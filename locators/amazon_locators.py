HOME_PAGE = {
    "search_box": "input#twotabsearchtextbox",
    "search_button": "input#nav-search-submit-button",
}

RESULTS_PAGE = {
    "brand_filter": lambda brand: f"//span[text()='{brand}']",
    "price_filter": lambda price: f"//span[text()='{price}']",
    "first_product": "(//div[@data-component-type='s-search-result']//h2/a)[1]",
}

PRODUCT_PAGE = {
    "add_to_cart": "#add-to-cart-button",
    "cart_count": "#nav-cart-count",
}

CART_PAGE = {
    "cart_subtotal": "#sw-subtotal, #sc-subtotal-amount-buybox",
}
