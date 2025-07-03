from behave import given, when, then
from ui.browser_setup import setup_browser
from ui.login_ui import login_via_ui
from ui.balance_ui import get_ui_balance
from api.login_api import get_api_token
from api.balance_api import get_api_balance
from ui.favorites_actions import *
import time

driver = None
game_card = None
USERNAME = ""
PASSWORD = ""

@given('I log in to gametwist as "{username}" with password "{password}"')
def step_impl(context, username, password):
    global driver, USERNAME, PASSWORD
    USERNAME = username
    PASSWORD = password
    driver = setup_browser()
    login_via_ui(driver, username, password)
    time.sleep(2)
    print(f"Logged in as {username}")

@then('the UI and API balances should match')
def step_impl(context):
    ui_balance = get_ui_balance(driver)
    token = get_api_token(USERNAME, PASSWORD)
    api_balance = get_api_balance(token)

    print(f"\n UI Balance:  {ui_balance}")
    print(f" API Balance: {api_balance}")
    assert ui_balance == api_balance, f"❌ Balance mismatch: UI={ui_balance}, API={api_balance}"
    print("Balances match")

@given('I open the casino page')
def step_impl(context):
    open_casino_page(driver)
    time.sleep(2)
    print("Casino page opened")

@then('the game "{game_name}" should be visible')
def step_impl(context, game_name):
    global game_card
    game_card = find_game_card(driver, game_name)
    assert game_card is not None, f"❌ Game '{game_name}' not found"
    print(f"Game '{game_name}' found")

@when('I mark the game "{game_name}" as favorite')
def step_impl(context, game_name):
    mark_favorite(driver, game_card)
    time.sleep(1)
    print(f"Marked '{game_name}' as favorite")

@then('it should appear as a favorite')
def step_impl(context):
    assert is_favorite(driver, game_card), "❌ Game is not marked as favorite"
    print("Game marked as favorite")

@when('I unmark the game "{game_name}" as favorite')
def step_impl(context, game_name):
    unmark_favorite(driver, game_card)
    time.sleep(1)
    print(f"Unmarked '{game_name}' as favorite")

@then('it should no longer appear as a favorite')
def step_impl(context):
    assert not is_favorite(driver, game_card), "❌ Game still marked as favorite"
    print("Game unmarked as favorite")
