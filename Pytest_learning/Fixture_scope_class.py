from selenium import webdriver
import pytest
driver = None
@pytest.fixture(scope='class')
def setup_browser(request):
    global driver
    driver = webdriver.Chrome("./chromedriver")
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup_browser")
class Base_class:
    pass
class Test_google(Base_class):
    def test_google(self):
        self.driver.get("https://www.google.com")
        assert True