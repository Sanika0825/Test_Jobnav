import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Initialize the Chrome driver
    _driver = webdriver.Chrome()
    _driver.maximize_window()
    
    # Yield the driver to the test
    yield _driver
    
    # Teardown: close the browser after test finishes
    _driver.quit()
