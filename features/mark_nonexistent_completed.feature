Feature: Attempt to mark a non-existent task as completed
  Scenario: Attempt to mark a non-existent task as completed
    Given the to-do list contains the task:
      | Task         |
      | Wash the car |
    When the user marks the task "Go to the gym" as completed
    Then an error should be shown indicating the task does