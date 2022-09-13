import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from Pageobjects.Homepage import Homepage
from Pageobjects.Checkoutpage import Checkoutpage
from Pageobjects.Confirmpage import confirmpage
from utilitis.Baseclass import Baseclass

#@pytest.mark.usefixtures("setup")
class Testone(Baseclass):
    def test_e2e(self):
        homepage=Homepage(self.driver)
        homepage.shopitems().click()
        logg=self.test_loggingdemo()


        #self.driver.find_element(By.LINK_TEXT, "Shop").click()
        confirmpages = confirmpage(self.driver)
        Checkoutpages= Checkoutpage(self.driver)
        products=Checkoutpages.getproducts()
        #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        i=-1
        for product in products:
            i=i+1
            prductText=product.text.strip()
            print(type(prductText)  )
            print(prductText)
            id = "Nokia Edge"
            if product.text == id:
                print ("Jaffa mani")
                Checkoutpages.getcardfooter()[i].click()
                #self.driver.find_elements(By.CSS_SELECTOR,".card-footer button")[i].click()

        #self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        Checkoutpages.getcheckoutbutton().click()
        self.driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()
        confirmpages.getcheckoutfunction().click()
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
        self.verifylinkpresence("India")
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.CSS_SELECTOR, ".checkbox.checkbox-primary").click()
        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

        print(self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text)


