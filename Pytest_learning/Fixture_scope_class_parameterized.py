from selenium import webdriver
import pytest

@pytest.fixture(scope='class',params=["chrome","firefox"])
def setup_method(request):
    if request.param == "chrome":
        driver = webdriver.Chrome("./chromedriver")

    if request.param == "firefox":
        driver = webdriver.Chrome("./chromedriver")
    request.cls.driver = driver
    yield
    driver.quit()
@pytest.mark.usefixtures('setup_method')
class Base_class:
    pass
class Test_google(Base_class):
    def test_google(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"

class Test_Facebook(Base_class):
    def test_facebook(self):
        self.driver.get("https://www.facebook.com")
        assert self.driver.title == "Facebook"
