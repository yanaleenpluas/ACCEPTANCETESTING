from behave import given, when, then
from todo_list import Task, ToDoSystem  # Asegúrate de que la importación sea correcta según tu estructura de archivos.

@given('the to-do list is empty')
def step_given_empty_todo_list(context):
    context.todo_system = ToDoSystem()

@when('the user adds a task "{task_name}" with description "{description}"')
def step_add_task(context, task_name, description):
    new_task = Task(task_name, 'pending', description)
    context.todo_system.addTask(new_task)

@then('the to-do list should contain "{task_name}" with description "{description}"')
def step_check_todo_list(context, task_name, description):
    tasks = context.todo_system.listTaskPending
    assert any(task.name == task_name and task.description == description for task in tasks), f'Task "{task_name}" not found in the to-do list'

@when('the user lists all tasks')
def step_list_all_tasks(context):
    context.todo_system.enumerateTasks()

@then('the output should contain:')
def step_check_output(context):
    expected_output = context.text
    assert expected_output.strip() in context.stdout_capture.getvalue().strip(), "Output does not match"

@when('the user marks task "{task_name}" as completed')
def step_mark_task_as_completed(context, task_name):
    tasks = context.todo_system.listTaskPending
    task_index = next((i for i, task in enumerate(tasks) if task.name == task_name), None)
    if task_index is not None:
        context.todo_system.markComplete(task_index)

@when('the user clears the to-do list')
def step_clear_todo_list(context):
    context.todo_system.clearList()

@when('the user edits task "{task_name}" with new name "{new_name}" and new description "{new_description}"')
def step_edit_task(context, task_name, new_name, new_description):
    tasks = context.todo_system.listTaskPending
    task_index = next((i for i, task in enumerate(tasks) if task.name == task_name), None)
    if task_index is not None:
        context.todo_system.editTask(task_index, new_name, new_description)

@when('the user shows details of task "{task_name}"')
def step_show_task_details(context, task_name):
    tasks = context.todo_system.listTaskPending
    task_index = next((i for i, task in enumerate(tasks) if task.name == task_name), None)
    if task_index is not None:
        context.todo_system.showTaskDetails(task_index)



@when(u'the user adds a task "Buy groceries"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user adds a task "Buy groceries"')


@then(u'the to-do list should contain "Buy groceries"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the to-do list should contain "Buy groceries"') 


@given(u'the to-do list contains tasks')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the to-do list contains tasks')


@then(u'the output should contain')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should contain')


@then(u'the to-do list should show task "Buy groceries" as completed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the to-do list should show task "Buy groceries" as completed')


@then(u'the to-do list should be empty')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the to-do list should be empty')