Feature: List all tasks in the to-do list
  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy Groceries |
      | Pay Bills     |
    When the user lists all tasks
    Then the output should contain:
      """
      Tasks:
      Buy Groceries
      Pay Bills
      """