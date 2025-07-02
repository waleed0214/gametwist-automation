import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_ui_balance(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='o-animated ']"))
    )
    elem = driver.find_element(By.XPATH, "//div[@class='c-balance o-grid o-grid--center o-grid--inline o-inset o-inset--24 c-header__balance']")
    text = elem.text.strip()
    digits = re.sub(r"[^\d]", "", text)  # Remove everything except numbers
    return int(digits)
