import time

from selenium.webdriver.common.by import By


class Test_items:
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    def test_button(self, browser):
        browser.get(self.link)
        time.sleep(30)
        button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
        assert button is not None, "Button doesn't exist"
