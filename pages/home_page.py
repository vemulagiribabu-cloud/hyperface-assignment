from constants.amazon_constants import AMAZON_URL
from locators.amazon_locators import HOME_PAGE
from playwright.async_api import TimeoutError


from constants.amazon_constants import AMAZON_URL
from playwright.async_api import TimeoutError

class HomePage:
    def __init__(self, page):
        self.page = page

    async def launch_site(self):
        print("Launching Amazon.in...")
        try:
            # Faster load trigger and higher timeout
            await self.page.goto(AMAZON_URL, timeout=60000, wait_until="domcontentloaded")

            # Try to handle any modals or popups
            await self.page.wait_for_timeout(3000)

            # Handle "Continue Shopping" or language modal
            modal_btns = self.page.locator("//input[@data-action-type='DISMISS']")
            if await modal_btns.count() > 0:
                print("Modal detected — clicking it")
                await modal_btns.first.click()
                await self.page.wait_for_timeout(1000)

            # Validate home page logo as load indicator
            await self.page.wait_for_selector("//a[@id='nav-logo-sprites']", timeout=20000)
            print("Amazon home page loaded successfully")

        except TimeoutError:
            print("Timeout while loading Amazon.in — attempting retry")
            await self.page.reload(wait_until="domcontentloaded")
            await self.page.wait_for_selector("//a[@id='nav-logo-sprites']", timeout=20000)
            print("Page loaded on retry")

        except Exception as e:
            raise AssertionError(f"Failed to load Amazon.in: {e}")


    async def search_product(self, product_name):
        print(f"Searching for product: {product_name}")
        try:
            # wait until header and search bar are visible
            await self.page.wait_for_selector(HOME_PAGE["search_box"], timeout=15000)
            await self.page.click(HOME_PAGE["search_box"], timeout=5000)
            await self.page.fill(HOME_PAGE["search_box"], product_name)
            await self.page.wait_for_timeout(1000)
            await self.page.click(HOME_PAGE["search_button"])

            # (Amazon keeps background requests alive)
            await self.page.wait_for_selector("div.s-main-slot", timeout=20000)
            print("Search executed successfully")
        except TimeoutError:
            await self.page.screenshot(path="debug_search_fail.png")
            raise AssertionError("Search box not found or not interactable. Screenshot saved.")
