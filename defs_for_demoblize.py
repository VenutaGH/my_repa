from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Def_for_demoblize:
    @staticmethod
    def login(browser, wait, username="12345", password="12345"):
        browser.get("https://demoblaze.com/index.html")
        wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
        wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys(username)
        browser.find_element(By.ID, "loginpassword").send_keys(password)
        browser.find_element(By.XPATH, "//button[text()='Log in']").click()
        wait.until(EC.text_to_be_present_in_element((By.ID, "nameofuser"), "Welcome"))

    @staticmethod
    def open_product_page(wait, product_name):
        product = wait.until(EC.element_to_be_clickable((By.XPATH, f'//a[text()="{product_name}"]')))
        product.click()
        title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2')))
        assert title.text == product_name

    @staticmethod
    def add_product_to_cart(wait):
        add_to_cart = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart")))
        add_to_cart.click()
        wait.until(EC.alert_is_present())
        wait._driver.switch_to.alert.accept()

    @staticmethod
    def open_cart(wait):
        cart = wait.until(EC.element_to_be_clickable((By.ID, "cartur")))
        cart.click()

    @staticmethod
    def assert_product_in_cart(wait, product_name):
        item = wait.until(EC.visibility_of_element_located((By.XPATH, f'//td[text()="{product_name}"]')))
        assert item.text == product_name
