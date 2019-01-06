from source.pages.home_page import HomePage
from source.pages.loginpage import LoginPage


def get_login_page(driver):
    login_page=LoginPage(driver)
    return login_page
def get_home_page(driver):
    home_page=HomePage(driver)
    return home_page