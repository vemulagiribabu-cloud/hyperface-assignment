from locators.amazon_locators import PRODUCT_PAGE

class ProductPage:
    def __init__(self, page):
        self.page = page

    async def add_to_cart(self, new_tab):
        print("Adding product to cart...")
        await new_tab.wait_for_selector(PRODUCT_PAGE["add_to_cart"])
        await new_tab.click(PRODUCT_PAGE["add_to_cart"])
        await new_tab.wait_for_timeout(2000)
        print("Product added to cart")
