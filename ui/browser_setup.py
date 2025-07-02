from selenium import webdriver

def setup_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
