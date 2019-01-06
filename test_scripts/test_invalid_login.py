from source.library import excel_automation as excel
from source.library.Constants import Constants
from source.pages import pagemanager as pm


class TestInValidLogin:
    def test_TC002_valid_login(self, request):
        username = excel.get_data(Constants.EXCEL_PATH, "Login", 1, "userName")
        password = excel.get_data(Constants.EXCEL_PATH, "Login", 1, "Password")
        title = excel.get_data(Constants.EXCEL_PATH, "Login", 1, "Title")
        expected_error_message=excel.get_data(Constants.EXCEL_PATH, "Login", 1, "ErrorMessage")

        login=pm.get_login_page(request.node.driver)
        login.login(username,password)
        login.verify_title(title)
        actual_error_message=login.get_error_message()
        login.verify_text(actual_error_message,expected_error_message)


