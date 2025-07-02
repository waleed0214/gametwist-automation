from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_casino_page(driver):
    driver.get("https://www.gametwist.com/de/casino/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'js-gameLink')]"))
    )

def find_game_card(driver, game_name):
    game_cards = driver.find_elements(By.XPATH, "//a[contains(@class, 'js-gameLink')]")
    for card in game_cards:
        if game_name.lower() in card.text.strip().lower():
            return card.find_element(By.XPATH, "..")  # Return parent div (the game card)
    return None

def mark_favorite(driver, game_card):
    try:
        heart_icon = game_card.find_element(By.XPATH, ".//a[contains(@class, 'c-game__fav')]")
        if "is-favorite" not in heart_icon.get_attribute("class"):
            heart_icon.click()
            print("✅ Marked as favorite")
        else:
            print("⚠️ Already marked as favorite")
    except Exception as e:
        print(f"❌ Could not mark favorite: {e}")

def unmark_favorite(driver, game_card):
    try:
        heart_icon = game_card.find_element(By.XPATH, ".//a[contains(@class, 'c-game__fav')]")
        if "is-favorite" in heart_icon.get_attribute("class"):
            heart_icon.click()
            print("✅ Unmarked as favorite")
        else:
            print("⚠️ Already unmarked")
    except Exception as e:
        print(f"❌ Could not unmark favorite: {e}")

def is_favorite(driver, game_card):
    heart_icon = game_card.find_element(By.XPATH, ".//a[contains(@class, 'c-game__fav')]")
    return "is-favorite" in heart_icon.get_attribute("class")
