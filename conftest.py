import pytest
from driver_module import Driver


@pytest.fixture
def browser_fixture():
    browser = Driver.setup_browser()
    yield browser

@pytest.fixture
def wait_fixture(browser_fixture):
    wait = Driver.wait(browser_fixture)
    yield wait
