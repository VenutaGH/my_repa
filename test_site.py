import pytest
from defs_for_demoblize import Def_for_demoblize as funcs

@pytest.mark.parametrize("product_name", [
    "Samsung galaxy s6",
    "Nokia lumia 1520",
    "Sony xperia z5"
])
def test_add_product_to_cart(browser_fixture, wait_fixture, product_name):
    funcs.login(browser_fixture, wait_fixture)
    funcs.open_product_page(wait_fixture, product_name)
    funcs.add_product_to_cart(wait_fixture)
    funcs.open_cart(wait_fixture)
    funcs.assert_product_in_cart(wait_fixture, product_name)