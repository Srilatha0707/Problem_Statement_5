import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.get("https://automationpanda.com/2021/12/29/want-to-practice-test-automation-try-these-demo-sites/")
    driver.maximize_window()
    driver.implicitly_wait(20)


@pytest.mark.usefixtures("driver_init")
class AutomationPanda_Test:
    pass


class Test_AutomationPanda_Title(AutomationPanda_Test):
    def test_title(self):
        assert self.driver.title == "Want to practice test automation? Try these demo sites! | Automation Panda"


class Test_w3schools_Speaking_Page(AutomationPanda_Test):
    def test_speaking_page(self):
        self.driver.find_element(By.CSS_SELECTOR, "#menu-item-10593").click()
        assert self.driver.title == "Speaking | Automation Panda"
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element(By.XPATH, "//h2[contains(text(),'Keynote Addresses')]"))
        time.sleep(2)
        keynote_addresses = self.driver.find_element(By.XPATH, "//h2[contains(text(),'Keynote Addresses')]")
        assert keynote_addresses.is_displayed()
        keynote_addresses_text = self.driver.find_element(By.CSS_SELECTOR,
                                                          ".wp-block-table.is-style-stripes").text
        if keynote_addresses_text:
            print(keynote_addresses_text)
            assert True
        else:
            print("keynote addresses doesn't contain text")
            assert False
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.ID, "conferences"))
        time.sleep(3)
        conference_talks = self.driver.find_element(By.ID, "conferences")
        assert conference_talks.is_displayed()
        conference_talks_text = self.driver.find_element(By.CSS_SELECTOR, ".wp-block-table.is-style-stripes").text
        if conference_talks_text:
            print(conference_talks_text)
            assert True
        else:
            print("conference talks doesn't contain text")
            assert False
