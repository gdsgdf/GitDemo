from selenium.webdriver.common.by import By
class Homepage():
    def __init__(self,driver):
        self.driver=driver

    shop= (By.LINK_TEXT, "Shop")
    name= (By.XPATH, "//div[@class='form-group']//input[@name='name']")
    email = (By.NAME, "email")
    Password=((By.CSS_SELECTOR, "#exampleInputPassword1"))
    checkbox=(By.CSS_SELECTOR, "#exampleCheck1")
    gender=(By.CSS_SELECTOR, "#exampleFormControlSelect1")
    radiobutton=(By.CSS_SELECTOR, "label[for='inlineRadio1']")
    submit=(By.CSS_SELECTOR, "input[value='Submit']")
    success=(By.XPATH, "//strong[normalize-space()='Success!']")

    def shopitems(self):
        return self.driver.find_element(*Homepage.shop)
    def getname(self):
        return self.driver.find_element(*Homepage.name)
    def getemail(self):
        return self.driver.find_element(*Homepage.email)
    def getPassword(self):
        return self.driver.find_element(*Homepage.Password)
    def getcheckbox(self):
        return self.driver.find_element(*Homepage.checkbox)
    def getradiobutton(self):
        return self.driver.find_element(*Homepage.radiobutton)
    def getsubmit(self):
        return self.driver.find_element(*Homepage.submit)
    def getgender(self):
        return self.driver.find_element(*Homepage.gender)
    def getsuccess(self):
        return self.driver.find_element(*Homepage.success)





    #self.driver.find_element(By.LINK_TEXT, "Shop").click()
