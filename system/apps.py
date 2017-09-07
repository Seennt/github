"""
Override Admin Config. to add additional custom
attributes.

E.g. glyphicon, registered for the navigation bar.

"""
from django.contrib.admin import apps


class SeenntAdminConfig(apps.AdminConfig):

    # Providing a glyphicon the navigation tab.
    glyphicon = 'log-in'

    # Register for navigation purpose.
    registered = 'navigation'
