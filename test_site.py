
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time





def login(browser, wait, username="12345", password="12345"):
    browser.get("https://demoblaze.com/index.html")
    wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys(username)
    browser.find_element(By.ID, "loginpassword").send_keys(password)
    browser.find_element(By.XPATH, "//button[text()='Log in']").click()
    time.sleep(10)


def test_add_s6_to_cart(browser, wait):
    login(browser, wait)
    galaxy_s6 = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Samsung galaxy s6"]')))
    galaxy_s6.click()

    title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2')))
    assert title.text == 'Samsung galaxy s6'


    add_to_cart = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart")))
    add_to_cart.click()


    wait.until(EC.alert_is_present())
    browser.switch_to.alert.accept()


    wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()


    item_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//td[text()="Samsung galaxy s6"]')))
    assert item_name.text == "Samsung galaxy s6"
