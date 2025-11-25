Feature: Login to account

Scenario: As a user I want to successfully login to the web portal and see the account dashboard
  Given User opening web page portal successfully
  When User entering valid 'ma1225@hotmail.com' username
  And User entering valid 'qa12345' password
  And User clicking on 'Sign in' button
  Then User is logged in and can see the account dashboard
