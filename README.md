# gametwist-automation
# 🎮 GameTwist Automation Suite

This is a test automation project for the GameTwist casino web application. It uses **Python**, **Selenium**, **Behave (BDD)**, and **API testing** to validate key features such as login, balance match, and favorite game functionality.

---

## Features Tested

-  Login with valid credentials (UI)
-  Compare UI vs API balance after login
-  Mark and unmark "Live Blackjack" as favorite
-  End-to-end UI + API test coverage

---

## Tech Stack

| Type         | Tool / Library              |
|--------------|-----------------------------|
| Language     | Python                      |
| UI Testing   | Selenium                    |
| BDD          | Behave                      |
| API Testing  | Requests                    |
| Reporting    | Behave Standard Output      |
| Browser      | Chrome (Chromedriver)       |
| Versioning   | Git + GitHub                |

---

## Project Structure

```bash
FunStageCode/
├── features/
│   ├── favorites.feature        # Gherkin scenarios
│   └── steps/steps.py           # Step definitions
├── ui/
│   ├── browser_setup.py         # Browser setup using Selenium
│   ├── login_ui.py              # UI login functions
│   ├── balance_ui.py            # Extract balance from UI
│   └── favorites_actions.py     # Favorite/unfavorite logic
├── api/
│   ├── login_api.py             # Get API auth token
│   └── balance_api.py           # Fetch API balance
├── .gitignore
└── README.md

---
**How to Run Tests**
Prerequisites
Python 3.x
Chrome browser installed
ChromeDriver compatible with your Chrome version
Git

Install Dependencies
pip install -r requirements.txt

(If you don’t have requirements.txt, manually install these:)
pip install selenium behave requests

**Run Tests**

From the project root:
behave

This will run all feature files in the features folder.
