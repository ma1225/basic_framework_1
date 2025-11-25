from ui.pages.locators.account_page_locators import AccountPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class AccountPage(AccountPageLocators):

    def __init__(self, driver):
        self.driver = driver

    def verify_account_page_displayed(self):

        assert WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.ACCOUNT_CONTENT)), (
            logger.error("Account content is not displayed on account screen!"))
