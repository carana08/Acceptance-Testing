Feature: Edit an existing task
  Scenario: Edit an existing task
    Given the to-do list contains the task:
      | Task    |
      | Buy milk|
    When the user edits the task "Buy milk" to "Buy bread"
    Then the to-do list should contain "Buy bread"
    And the to-do list should not contain "Buy milk"