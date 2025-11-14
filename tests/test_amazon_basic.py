import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pages.home_page import HomePage
from pages.results_page import ResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from constants.amazon_constants import DEFAULT_SEARCH_TERM, DEFAULT_BRAND, DEFAULT_PRICE_RANGE

async def test_amazon_end_to_end_experience(page):
    home_page = HomePage(page)
    results_page = ResultsPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    # Step 1: Launch and search
    await home_page.launch_site()
    await home_page.search_product(DEFAULT_SEARCH_TERM)

    # Step 2: Filter and open product
    await results_page.apply_filters(DEFAULT_BRAND, DEFAULT_PRICE_RANGE)
    new_tab = await results_page.open_first_product()

    # Step 3: Add to cart and validate
    await product_page.add_to_cart(new_tab)
    await cart_page.validate_cart(new_tab)
