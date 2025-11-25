from selenium import webdriver

def before_all(context):
  """
  Setup a browser instance before any tests start.
  """
  context.driver = webdriver.Chrome()

def after_all(context):
  """
  Close the browser after all tests have finished.
  """
  context.driver.quit()