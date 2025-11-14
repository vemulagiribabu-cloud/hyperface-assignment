from locators.amazon_locators import PRODUCT_PAGE, CART_PAGE

class CartPage:
    def __init__(self, page):
        self.page = page

    async def validate_cart(self, new_tab):
        print("Validating cart contents")
        cart_count = await new_tab.inner_text(PRODUCT_PAGE["cart_count"])
        subtotal = await new_tab.inner_text(CART_PAGE["cart_subtotal"])
        print(f"Cart count: {cart_count}")
        print(f"Cart subtotal: {subtotal}")
        assert int(cart_count) >= 1, "Cart should have at least 1 item"
        assert subtotal.strip() != "", "Cart subtotal should not be empty"
