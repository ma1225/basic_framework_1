from selenium.webdriver.common.by import By

class LoginPageLocators:

    LOGIN_HEADER = (By.CSS_SELECTOR, "h4.auth-header")
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BUTTON = (By.ID, "log-in")
