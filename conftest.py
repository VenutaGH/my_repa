import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait





@pytest.fixture
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser

@pytest.fixture
def wait(browser):
    wait = WebDriverWait(browser, 15)
    yield wait
