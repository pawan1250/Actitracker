from selenium.webdriver.common.by import By
from allure import step
from source.pages.basepage import BasePage

class LoginPage(BasePage):
    __username=(By.ID,"username")
    __password=(By.NAME,"pwd")
    __login_button=(By.ID, "loginButton")
    __error_message=(By.XPATH,"//span[@class='errormsg' and not(@id='errorspan')]")
    @step
    def login(self,userName,passWord):
        self.driver.find_element(*self.__username).send_keys(userName)
        self.driver.find_element(*self.__password).send_keys(passWord)
        self.driver.find_element(*self.__login_button).click()

    def get_error_message(self):
        self.wait_for_element_to_presence(self.__error_message)
        error_value=self.driver.find_element(*self.__error_message).text
        return error_value