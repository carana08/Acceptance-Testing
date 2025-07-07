from behave import given, when, then
from todo_list import TodoList

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = TodoList()

@given('the to-do list contains tasks')
def step_impl(context):
    context.todo_list = TodoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'])

@given('the to-do list contains the tasks')
def step_impl(context):
    context.todo_list = TodoList()
    for row in context.table:

        task_name = row['Task']
        status = row.get('Status', 'Pending')
        context.todo_list.tasks.append(
            context.todo_list.__class__.__bases__[0].__subclasses__()[0](task_name, status)
            if hasattr(context.todo_list, 'Task') else
            type('Task', (), {'name': task_name, 'status': status})()
        ) if False else context.todo_list.add_task(task_name)

@given('the to-do list contains the task')
def step_impl(context):
    context.todo_list = TodoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'])

@when('the user add a task "{task}"')
def step_impl(context, task):
    context.todo_list.add_task(task)

@when('the user lists all tasks')
def step_impl(context):
    tasks = context.todo_list.list_tasks()
    context.output = "Tasks:\n" + "\n".join(task.name for task in tasks)

@when('the user marks task "{task}" as completed')
@when('the user marks the task "{task}" as completed')
def step_impl(context, task):
    result = context.todo_list.mark_completed(task)
    if not result:
        context.error = f'Task "{task}" does not exist.'

@when('the user clears the to-do list')
def step_impl(context):
    context.todo_list.clear()

@when('the user edits the task "{old}" to "{new}"')
def step_impl(context, old, new):
    context.todo_list.edit_task(old, new)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    assert context.todo_list.contains(task)

@then('the to-do list should not contain "{task}"')
def step_impl(context, task):
    assert not context.todo_list.contains(task)

@then('the output should contain')
def step_impl(context):
    expected_lines = [line.strip().lower() for line in context.text.strip().splitlines()]
    actual_lines = [line.strip().lower() for line in context.output.strip().splitlines()]
    assert expected_lines == actual_lines

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    t = context.todo_list.get_task(task)
    assert t is not None
    assert t.status == "Completed"

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_list.list_tasks()) == 0

@then('an error should be shown indicating the task does')
def step_impl(context):
    assert hasattr(context, 'error')
    assert "does not exist" in context.error