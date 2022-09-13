
import pytest
from _pytest import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import logging

@pytest.mark.usefixtures("setup")
class Baseclass:


     def verifylinkpresence(self,text):
          wait = WebDriverWait(self.driver,10)
          wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

     def SelectoptionbyText(self,locator,text):
          sel = Select(locator)
          sel.select_by_visible_text(text)

     def test_loggingdemo(self):
          logger = logging.getLogger(__name__)
          filehandler = logging.FileHandler("logfile")  # logfile is file name to store the logs
          formatter = logging.Formatter("%(asctime)s :%(levelname)s: %(name)s:%(message)s")
          filehandler.setFormatter(formatter)
          logger.addHandler(filehandler)  # filehandler object
          logger.setLevel(logging.INFO)
          logger.debug("it is a debug statement")
          logger.info("information")
          logger.warning("it's a precaution")
          logger.error("assertion error")
          logger.critical("it's a critical")



