import pytest
from source.library import  webdriver_manager as wb, generic
from source.library import excel_automation as excel
from source.library.Constants import Constants

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtime_maker_report(item,call):
    outcome=yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="function", autouse=True)
def set_up(request):
    url=excel.get_data(Constants.EXCEL_PATH, "Setting", 0, "URL")
    browser_name=excel.get_data(Constants.EXCEL_PATH, "Setting", 0, "BrowserName")
    driver=wb.get_driver(browser_name,url)
    if request.node.driver is not None:
        request.node.driver=driver
    yield
    if request.node.rep_call.failed:
        generic.attach_screen_shot(driver,request.function.__name__)
    driver.quit()