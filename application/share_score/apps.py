from django.apps import AppConfig


class ShareScoreConfig(AppConfig):
    name = 'application.share_score'

    # Provide a verbose name for human readable(spaces, etc.)
    verbose_name = 'Share score'

    # Add to dropdown button
    site = True

    # Register for navigation purpose.
    registered = True
