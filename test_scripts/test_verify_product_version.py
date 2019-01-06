from source.library import excel_automation as excel
from source.library.Constants import Constants
from source.pages import pagemanager as pm

class TestVerifyProductVersion:
    def test_TC003_verify_product_version(selfself,request):
        username = excel.get_data(Constants.EXCEL_PATH, "Login", 0, "UserName")
        password = excel.get_data(Constants.EXCEL_PATH, "Login", 0, "Password")
        title = excel.get_data(Constants.EXCEL_PATH, "Login", 0, "Title")
        expected_product_version=excel.get_data(Constants.EXCEL_PATH,"Login",0,"ProductVersion")

        login=pm.get_login_page(request.node.driver)
        login.login(username,password)
        login.verify_title(title)

        home=pm.get_home_page(request.node.driver)
        actual_product_version=home.get_product_version()
        home.verify_text(actual_product_version,expected_product_version)
        home.close_product_version_pop_up()
        home.click_logout_link()
