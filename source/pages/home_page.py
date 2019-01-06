
from source.pages.basepage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    __help_menu=(By.XPATH,"//div[normalize-space/(text())='Help']")
    __about_actitime=(By.XPATH,"//a[text()='About your actiTime']" )
    __product_version=(By.XPATH,"//span[@class='productVersion']")
    __close_pop_up=(By.CSS_SELECTOR,"div#aboutPopupCloseButtonId")

    def get_product_version(self):
        self.driver.find_element(*self.__help_menu).click()
        self.driver.find_element(*self.__about_actitime).click()
        version=self.driver.find_element(*self.__product_version).text
        return version
    def close_product_version_pop_up(self):
        self.driver.find_element(*self.__close_pop_up).click()

