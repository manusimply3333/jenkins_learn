# import pytest
# from selenium import webdriver
# @pytest.mark.usefixtures('setup_method')
# class Base_class:
#     pass
# class Test_with_parameter(Base_class):
#
#     def test_google(self):
#         self.driver.get("https://www.google.com")
#     def test_facebook(self):
#         self.driver.get("https://www.facebook.com")
#
#     @pytest.mark.parametrize("a,b", [(1, 2), (3, 4)])
#     def test_param(self,a,b):
#         assert a + b == 3

import pytest
from selenium import webdriver

# @pytest.fixture(scope="module",params=["chrome","firefox"])
# def browser(request):
#     if request.param == "chrome":
#         driver = webdriver.Chrome("./chromedriver")
#     else:
#         driver = webdriver.Chrome("./chromedriver")
#     request.cls.driver = driver
#     yield
#     print("driver quit")
#     request.cls.driver.quit()
# @pytest.mark.usefixtures("browser")
# class Baseclass:
#     pass
# class Test_browse(Baseclass):
#
#     def test_google(self):
#         print("driver launched")
#         self.driver.get("https://www.google.com")
#
#     def test_firefox(self):
#         print("driver launched")
#         self.driver.get("https://www.google.com")
#
#     @pytest.mark.parametrize("a,b", [(1, 2), (3, 0)])
#     def test_assert(self,a,b):
#         print("inside parametrized")
#         assert a + b == 3

#driver = webdriver.Chrome("./chromedriver")
for i in range(0,5):
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://www.google.com")

driver.quit()