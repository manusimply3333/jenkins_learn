from selenium import webdriver
import pytest
web_driver = None
@pytest.fixture
def driver():
    global web_driver
    web_driver = webdriver.Chrome("./chromedriver")
    yield
    web_driver.quit()
    #return web_driver
    #return web_driver
@pytest.mark.usefixtures('driver')
def test_google():
    web_driver.get("https://www.google.com")
    print("This is for google")
    #driver.quit()
@pytest.mark.usefixtures('driver')
def test_facebook():
    web_driver.get("https://www.facebook.com")
    print("This is for facebook")
    #driver.quit()
@pytest.mark.usefixtures('driver')
def test_youtube():
    web_driver.get("https://www.youtube.com")
    print("This is for youtube")
    #driver.quit()
def test_instagram(driver):
    web_driver.get("https://www.instagram.com")
    print("This is for youtube")
    #driver.quit()
def test_no():
    assert True
def test_yes():
    assert False
def test_np():
    assert True
def test_yp():
    assert True