import asyncio
from playwright.async_api import Page, TimeoutError as PlaywrightTimeoutError


class ResultsPage:
    def __init__(self, page: Page):
        self.page = page
        # Use a broad but stable selector for product links
        self.product_selector = "a.a-link-normal.s-line-clamp-2.s-link-style.a-text-normal"

    async def apply_filters(self, brand_name: str, price_range: str):
        print(f"Applying filters: {brand_name}, {price_range}")

        # --- Wait for filter sidebar to be ready ---
        await self.page.wait_for_selector("#s-refinements", timeout=20000)

        # --- Apply brand filter ---
        try:
            brand_filter = self.page.locator(f"//span[text()[contains(., '{brand_name}')]]").first
            await brand_filter.scroll_into_view_if_needed()
            await asyncio.sleep(1)
            await brand_filter.click(force=True)
            print(f"Clicked brand filter: {brand_name}")
            await self.page.wait_for_load_state("networkidle")
        except Exception as e:
            print(f"Brand filter '{brand_name}' not found — {e}")

        # --- Apply price filter (try either range or manual) ---
        try:
            price_filter = self.page.locator(f"//span[contains(text(), '{price_range}')]").first
            await price_filter.scroll_into_view_if_needed()
            await asyncio.sleep(1)
            await price_filter.click(force=True)
            print(f"Clicked price filter: {price_range}")
            await self.page.wait_for_load_state("networkidle")
        except Exception as e:
            print(f"Price filter '{price_range}' not found — {e}")

        # --- Wait for results after filters applied ---
        for attempt in range(3):
            print(f"Waiting for search results... (Attempt {attempt+1}/3)")
            try:
                await self.page.wait_for_selector(self.product_selector, timeout=15000)
                count = await self.page.locator(self.product_selector).count()
                if count > 0:
                    print(f"Found {count} products after filtering")
                    return
            except PlaywrightTimeoutError:
                print("Results not visible yet — retrying")
                await self.page.mouse.wheel(0, 3000)
                await asyncio.sleep(2)

        print("Debug: No visible products found even after retries")
        raise AssertionError("Products did not appear after applying filters.")

    async def open_first_product(self):
        print("Opening first visible product")

        try:
            product = self.page.locator(self.product_selector).first
            await product.scroll_into_view_if_needed()
            product_name = await product.locator("h2 span").text_content(timeout=15000)
            print(f"Found product: {product_name[:80]}...")

            # Open in new tab
            async with self.page.context.expect_page() as new_page_info:
                await product.click()
            new_tab = await new_page_info.value
            await new_tab.wait_for_load_state("domcontentloaded")
            print("Product page opened successfully in new tab")
            return new_tab
        except Exception as e:
            print(f"Failed to open product: {e}")
            raise
