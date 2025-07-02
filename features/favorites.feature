Feature: Verify login, balance, and favorite functionality

  Scenario: Login and verify balance
    Given I log in to gametwist as "petergreener" with password "qwer1234"
    Then the UI and API balances should match

  Scenario: Mark and unmark "Live Blackjack" as favorite
    Given I open the casino page
    Then the game "Live Blackjack" should be visible
    When I mark the game "Live Blackjack" as favorite
    Then it should appear as a favorite
    When I unmark the game "Live Blackjack" as favorite
    Then it should no longer appear as a favorite
