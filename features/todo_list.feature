Feature: To-Do List Manager

Scenario: Add a task to the to-do list
  Given the to-do list is empty
  When the user adds a task "Buy groceries"
  Then the to-do list should contain "Buy groceries"

Scenario: List all tasks in the to-do list
  Given the to-do list contains tasks:
    | Task         | Status  | Description                        |
    | Buy groceries| Pending | Purchase items at the store        |
  When the user lists all tasks
  Then the output should contain:
    """
    Tasks:
    1. Buy groceries (Pending)
    """

Scenario: Mark a task as completed
  Given the to-do list contains tasks:
    | Task         | Status  | Description                        |
    | Buy groceries| Pending | Purchase items at the store        |
  When the user marks task "Buy groceries" as completed
  Then the to-do list should show task "Buy groceries" as completed

Scenario: Clear the entire to-do list
  Given the to-do list contains tasks:
    | Task         | Status  | Description                        |
    | Buy groceries| Pending | Purchase items at the store        |
  When the user clears the to-do list
  Then the to-do list should be empty

Scenario: Edit an existing task
  Given the to-do list contains tasks:
    | Task         | Status  | Description                        |
    | Buy groceries| Pending | Purchase items at the store        |
  When the user edits task "Buy groceries" with new name "Buy vegetables" and new description "Purchase fresh vegetables"
  Then the to-do list should contain "Buy vegetables" with description "Purchase fresh vegetables"

Scenario: Show details of a task
  Given the to-do list contains tasks:
    | Task         | Status  | Description                        |
    | Buy groceries| Pending | Purchase items at the store        |
  When the user shows details of task "Buy groceries"
  Then the output should contain:
    """
    Task Details:
    Name: Buy groceries
    Status: Pending
    Description: Purchase items at the store
    """
