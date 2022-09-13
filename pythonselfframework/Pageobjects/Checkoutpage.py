from selenium.webdriver.common.by import By


class Checkoutpage():

    def __init__(self,driver):
        self.driver=driver

    productslist= (By.XPATH, "//div[@class='card h-100']")
    cardfooter=(By.CSS_SELECTOR,".card-footer button")
    checkoutitem=(By.CSS_SELECTOR, ".nav-link.btn.btn-primary")


    def getproducts(self):
        return self.driver.find_elements(*Checkoutpage.productslist)

    def getcardfooter(self):
        return self.driver.find_elements(*Checkoutpage.cardfooter)
    def getcheckoutbutton(self):
        return self.driver.find_element(*Checkoutpage.checkoutitem)

    #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")