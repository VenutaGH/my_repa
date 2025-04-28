from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.get('https://www.qa-practice.com/elements/button/simple')

#click_button = browser.find_element(By.ID,'submit-id-submit')
#click_button.click()
#sleep(5)

#click_button1 = browser.find_element(By.CLASS_NAME, '')
#click_button1.click()
#sleep(5)

# element = browser.find_element(By.LINK_TEXT, 'Contact')
# browser.execute_script("arguments[0].scrollIntoView(true);", element)
# sleep(1)
# element.click()
#
# sleep (5)
#
#
click_button4 = browser.find_element(By.XPATH, '//input[@class="btn btn-primary"]')
click_button4.click()

#
# click_button3= browser.find_element(By.CSS_SELECTOR, '')
# click_button3.click()