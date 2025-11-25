This is example for basic framework design:

1) In order to run tests please install libraries from requirements.txt (behave, selenium, requests, pytest):

pip install -r requirements.txt

2) For UI BDD with Gherkin (login_steps.py) run 'behave' on terminal
   For API test with pytest (test_generate_token_and_create_booking.py) run 'pytest' on terminal

Framework structure:
---------------------

API: (Used API's from https://restful-booker.herokuapp.com/apidoc/index.html)
-----------------------------------------------------------------------------
api --> api_calls(auth_token.py, booking_management.py)
        api_impl(auth_token_impl.py, booking_management_impl.py)
        tests (test_generate_token_and_create_booking.py)


UI + Gherkin BDD: (Used site of https://demo.applitools.com/)
-------------------------------------------------------------
features --> steps(login_steps.py)
             environment.py
             login.feature

ui --> pages(login_page.py, account_page.py) --> locators (login_page_locators.py, account_page_locators.py)
       tests
       conftest.py

Utils:
------
utils --> configs (url_links.py)
          helpers (random_generator.py)

Others:
-------
pytest.ini
readme.txt
requirements.txt
