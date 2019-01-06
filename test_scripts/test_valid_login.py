from source.library import excel_automation as excel
from source.library.Constants import Constants
from source.pages import pagemanager as pm

class TestLogin:
    def test_TC001_valid_login(self, request):
        username=excel.get_data(Constants.EXCEL_PATH,"Login",0,"UserName")
        password=excel.get_data(Constants.EXCEL_PATH,"Login",0,"Password")
        title=excel.get_data(Constants.EXCEL_PATH,"Login",0,"Title")

        login = pm.get_login_page(request.node.driver)
        login.login(username, password)
        login.verify_title(title)

