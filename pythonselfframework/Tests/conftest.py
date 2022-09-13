import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service



@pytest.fixture(scope="class")

def setup(request):
    service_obj = Service("C:\Program Files\Python310\chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver

    yield
    driver.close()




