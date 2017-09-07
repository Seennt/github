# -*- coding: utf-8 -*-
""" Module: applications as part of: applications

Created by: Reinier on 5-2-2017. Installed application to display in top navigation.

Examples:
    Should be defined in a later state.

Attributes:
    All module attributes defined to understand there meaning.

TODO:
    - Use TODO comments for code that is temporary, a short-term solution, or good-enough but not perfect.
    
"""
from django.apps import apps


class Item(object):
    """
    Collect 'verbose_name' of a package.
    """

    def __init__(self, application):
        """
        Constructor for Label

        """
        self.name = self.name(application)
        self.site = self.site(application)
        self.verbose_name = self.verbose(application)
        self.glyphicon = self.glyphicon(application)

    @staticmethod
    def name(application):
        """
        Method: name()
        Get the application name for the corresponding application.

        --------------------------------------------------
        :rtype: str
        """

        if hasattr(application, 'name') and application.name:
            try:
                name = application.name.split('.')[-1].replace('_', '-')
            except IndexError:
                raise Exception('No application name is defined.')

            return name

    @staticmethod
    def site(application):
        """
        Method: site()
        Add the application to the dropdown box "Sites"

        --------------------------------------------------
        :rtype: str
        """

        if hasattr(application, 'site') and application.site:
            return application.site

    @staticmethod
    def verbose(application):
        """
        Method: verbose()
        Get the verbose name of the application.

        --------------------------------------------------
        :rtype: str
        """
        if hasattr(application, 'verbose_name') and application.verbose_name:
            return application.verbose_name

    @staticmethod
    def glyphicon(application):
        """
        Method: glyphicon()
        Get the glyphicon of the application.

        --------------------------------------------------
        :rtype: str
        """
        if hasattr(application, 'glyphicon') and application.glyphicon:
            return application.glyphicon


class Labels(object):
    """
    Get a list of registered applications objects.

    """

    def __init__(self):
        """
        Constructor for Labels

        """
        self.labels = []

    def process(self):
        """
        Process all registered Labels

        """

        for application in apps.get_app_configs():
            if hasattr(application, 'registered') and application.registered:
                label = Item(application)

                self.labels.append(label)

        return reversed(self.labels)


class Sites(object):
    """
    Get a list of sites.

    """

    def __init__(self):
        """
        Constructor for Sites

        """
        self.sites = []

    def process(self):
        """
        Process all registered Sites

        """

        for application in apps.get_app_configs():
            if hasattr(application, 'site') and application.site:
                site = Item(application)

                self.sites.append(site)

        return self.sites
