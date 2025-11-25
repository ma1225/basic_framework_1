from ui.pages.locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class LoginPage(LoginPageLocators):

    def __init__(self, driver):
        self.driver = driver

    def open_portal_and_verify_it_displayed(self, url):

        self.driver.get(url)
        assert WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.LOGIN_HEADER)), (
            logger.error("Login header is not displayed on login screen!"))

    def enter_username_to_username_field(self, username):

        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password_to_password_field(self, password):

        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_on_sign_in_button(self):

        self.driver.find_element(*self.SIGN_IN_BUTTON).click()
