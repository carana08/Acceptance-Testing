Feature: Add a task to the to-do list

Scenario: Add  a task to the to-do list  
  Given the to-do list is empty
  When the user add a task "Buy Groceries"
  Then the to-do list should contain "Buy Groceries"