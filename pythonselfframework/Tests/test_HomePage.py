import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from utilitis.Baseclass import Baseclass
from Pageobjects. Homepage import Homepage


class TestHomepage(Baseclass):
    def test_formSubmiison(self,getdata):
        log=self.test_loggingdemo()
        self.driver.get("https://www.rahulshettyacademy.com/angularpractice/")
        homepage = Homepage(self.driver)

        #log.info("firstname is" + getdata["firstname"])
        homepage.getname().send_keys(getdata["firstname"])
        #driver.find_element(By.XPATH, "//div[@class='form-group']//input[@name='name']").send_keys("laxmi")
        #driver.find_element(By.NAME, "email").send_keys("ramalakshmict@gmail.com")
        homepage.getemail().send_keys(getdata["lastname"])

        #driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("12345")
        homepage.getPassword().send_keys("12345")
        #driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
        homepage.getcheckbox().click()
        #sel = Select(self.driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
        self.SelectoptionbyText(homepage.getgender(),getdata["gender"])
        #driver.find_element(By.CSS_SELECTOR, "label[for='inlineRadio1']").click()
        homepage.getradiobutton().click()
        #driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
        homepage.getsubmit().click()
        #alertmsg = self.driver.find_element(By.XPATH, "//strong[normalize-space()='Success!']").text
        alertmsg = homepage.getsuccess().text
        print(alertmsg)
        assert "Success" in alertmsg

    @pytest.fixture(params=HomePageData.GetTestData("testcase2"))
    def getdata(self,request):
        return request.param



