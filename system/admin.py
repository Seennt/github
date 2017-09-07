# coding=utf-8
"""
Custom Administration interface.

Set up your own admin site with custom behavior, you’re free to
subclass AdminSite and override or add anything you like.

Add the following lines to urls.py:
    admin.site = admin_site
    admin.sites.site = admin.site
    admin.autodiscover()

Register app in INSTALLED_APPS:
    project.apps.SeenntAdminConfig'

"""
from django.contrib.admin import *


# ----------------------------------------------------------------------------------------
# Customizing Django admin.
# ----------------------------------------------------------------------------------------
class SeenntAdmin(AdminSite):
    site_header = 'Seennt administration'
    site_title = 'SEENNT'

    def __init__(self, *args, **kwargs):
        super(SeenntAdmin, self).__init__(*args, **kwargs)
        self._registry.update(site._registry)

    def __str__(self):
        return self.__class__.__name__

site = SeenntAdmin()
