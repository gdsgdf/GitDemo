from selenium.webdriver.common.by import By

class confirmpage():
    def __init__(self,driver):
        self.driver=driver
    checkoutfunction= (By.CSS_SELECTOR,".btn.btn-success")
    def getcheckoutfunction(self):
        return self.driver.find_element(*confirmpage.checkoutfunction)
    #self.driver.find_element(By.LINK_TEXT, "Shop").click()







