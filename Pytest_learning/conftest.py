import pytest
from selenium import webdriver
@pytest.fixture(scope='class',params=["chrome","firefox"])
def setup_method(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome("./chromedriver")
    if request.param == 'firefox':
        driver = webdriver.Chrome("./chromedriver")
    request.cls.driver = driver
    yield
    driver.quit()

