from django.apps import AppConfig


class OrganizeConfig(AppConfig):
    name = 'application.organize'

    # Add to dropdown button
    site = True

    # Register for navigation purpose.
    registered = True
