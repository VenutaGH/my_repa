from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Driver:
    @staticmethod
    def setup_browser():
        browser = webdriver.Firefox()
        browser.maximize_window()
        return browser

    @staticmethod
    def wait(browser):
        wait = WebDriverWait(browser, 15)
        return wait

