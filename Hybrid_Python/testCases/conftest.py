import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime

@pytest.fixture(scope="session")
def setup():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("start-maximized")
    service = ChromeService(executable_path="C:\\Users\\ramesh.ganamana\\Downloads\\chromedriver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    time.sleep(5)
    yield driver
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if 'setup' in item.funcargs:
        driver = item.funcargs['setup']
        screenshots = ScreenShots(driver)
        pytest_html = item.config.pluginmanager.getplugin('html')
        extra = getattr(report, 'extra', [])

        if report.when in ['call', 'setup']:
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "@").replace("/", "@")
                file_list1 = file_name.split("@")
                file_path = screenshots.take_screenshot(driver, file_list1[-1], file_list1[1])

                if file_path:
                    html = (
                            '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                            'onclick="window.open(this.src)" align="right"/></div>' % file_path.replace("%20", "%2520")
                    )
                    extra.append(pytest_html.extras.html(html))

                report.extra = extra


class ScreenShots:
    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, driver, testcase_name="", module_name=""):
        test_name = testcase_name.replace(" ", "_")
        date = datetime.datetime.now().strftime("%I_%M%p_on_%B_%d_%Y")
        screen_shot_folder_path = os.path.abspath('.') + "\\reports\\Screenshots"

        if not os.path.exists(screen_shot_folder_path):
            os.makedirs(screen_shot_folder_path)

        file_path = os.path.join(screen_shot_folder_path, f"{testcase_name}{module_name}_{date}.png")
        driver.save_screenshot(file_path)
        return os.path.relpath(file_path, os.path.abspath('.'))
