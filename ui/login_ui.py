from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_via_ui(driver, username, password):
    driver.get("https://www.gametwist.com")

    # Wait for cookie banner and accept
    try:
        accept_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        accept_btn.click()
    except:
        print("⚠️ Cookie banner not shown or already accepted.")

    # Click login button in header
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'c-btn--header')]"))
    ).click()

    # Wait for username field and send credentials
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(username)
    pw_field = driver.find_element(By.ID, "password")
    pw_field.send_keys(password)
    pw_field.send_keys(Keys.ENTER)

    # Wait for login to complete (e.g. by checking presence of balance or avatar)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='c-balance o-grid o-grid--center o-grid--inline o-inset o-inset--24 c-header__balance']"))
    )
