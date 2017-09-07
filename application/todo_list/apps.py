from django.apps import AppConfig


class TodoListConfig(AppConfig):
    name = 'application.todo_list'

    # Provide a verbose name for human readable(spaces, etc.)
    verbose_name = 'To do list'

    # Add to dropdown button
    site = True

    # Register for navigation purpose.
    registered = True
