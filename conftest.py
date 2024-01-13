import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    browser.config.window_width = 1920
    browser.config.window_height = 1200
    yield
    browser.quit()
