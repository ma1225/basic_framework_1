from behave import *
from ui.pages.account_page import AccountPage
from ui.pages.login_page import LoginPage
from utils.configs import url_links
import logging

logger = logging.getLogger(__name__)

@given("User opening web page portal successfully")
def step_given_user_open_portal_successfully(context):

    context.url = url_links.get_base_url()
    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)

    context.login_page.open_portal_and_verify_it_displayed(context.url)

@when("User entering valid '{username}' username")
def step_when_user_entering_username(context, username):

    logger.info("Enter username to username field")
    context.login_page.enter_username_to_username_field(username)

@when("User entering valid '{password}' password")
def step_when_user_entering_username(context, password):

    logger.info("Enter password to password field")
    context.login_page.enter_password_to_password_field(password)

@when("User clicking on 'Sign in' button")
def step_when_user_click_on_sign_in_button(context):

    context.login_page.click_on_sign_in_button()

@then("User is logged in and can see the account dashboard")
def step_then_user_logged_in(context):

    context.account_page = AccountPage(context.driver)

    context.account_page.verify_account_page_displayed()
    #context.driver.quit()
