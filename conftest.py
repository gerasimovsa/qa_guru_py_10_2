import pytest
from selene import browser


@pytest.fixture
def browser_settings():
    browser.driver.set_window_size(1920, 1200)


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown(browser_settings):
    browser.open("https://google.com")
    yield
    browser.quit()
