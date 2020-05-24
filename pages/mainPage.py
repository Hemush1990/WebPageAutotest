from data.locators import Locator
from selenium.webdriver.common.by import By

from testSuit.conftest import url
from .basepage import BasePage


class Mainpage(BasePage):


    #get the bumber of HTML forms
    def count_forms(self):
        formexist = self.browser.find_elements(By.XPATH, Locator.formelement)
        print("The number of forms on the site are: ",  len(formexist))


    #get the number of img tags
    def count_img(self):
        imgexist = self.browser.find_elements(By.XPATH, Locator.imgelement)
        print("\nThe number of tag images on the page is: ",  len(imgexist))


