from django.apps import AppConfig


class CollectConfig(AppConfig):
    name = 'utility.collect'

    # Provide a verbose name for human readable(spaces, etc.)
    verbose_name = 'Collector'

    # Add to dropdown button
    site = True

    # Register for navigation purpose.
    registered = True
