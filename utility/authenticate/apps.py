from django.apps import AppConfig


class AuthenticateConfig(AppConfig):
    name = 'utility.authenticate'

    # Providing a glyphicon the navigation tab.
    glyphicon = 'log-out'

    # Register for navigation purpose.
    registered = True

    # Human readable name
    verbose_name = 'Logout'
