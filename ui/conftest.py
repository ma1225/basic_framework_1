from selenium import webdriver
import pytest
import os

@pytest.fixture(scope="session")
def init_driver(request):

    driver = ""
    supported_browsers = ['chrome', 'firefox']

    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set!")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser {browser} is not one of the supported browsers. " f"Supported browser are: {supported_browsers}")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    driver.quit()
