# -*- coding: utf-8 -*-
""" Module: packages as part of: application

Created by: Reinier on 5-2-2017. Installed applications to display in top navigation. The list of sites will
be displayed in a drop down list, the list of labels are displayed as tabs within the top navigation bar.

Examples:
    Define in apps.py:
            # Providing a glyphicon the navigation tab.
            glyphicon = 'log-in'

            # Provide a verbose name for human readable(spaces, etc.)
            verbose_name = 'To do list'

            # Register for navigation purpose.
            registered = 'navigation'

            # Add to dropdown button
            site = True

Attributes:
    All module attributes defined to understand there meaning.

TODO:
    - Use TODO comments for code that is temporary, a short-term solution, or good-enough but not perfect.
    
"""
from django.apps import apps


class Item(object):
    """: The class: "Item", is part of module: "packages".

    Provide a class description here. A good explanation of a class provides a higher readability of the code.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.

    """

    def __init__(self, application):
        """12-10-2017: The method: "__init__", is part of class: "Item".

        A constructor method for the Item class. This item is part of a factory pattern.

        Args:
            name (str) : Name for a specific item.
            site (str) : A dict of value and keys meant for the whole class.
            verbose_name (str) : Human readable application name
            glyphicon (str) : Glyphicon name.

        Returns:
            object: Object(Item) with a list of navigation items.

        """
        self.name = self.item_name(application)
        self.site = self.item_site(application)
        self.verbose_name = self.item_verbose(application)
        self.glyphicon = self.item_glyphicon(application)

    @staticmethod
    def item_name(application):
        """12-10-2017: The method: "item_name", is part of class: "Item".

        Collect the application name and remove "application" and "_".

        Returns:
            str: Clean name of application.

        Raises:
            IndexError: Raised when a sequence subscript is out of range.

        """
        if hasattr(application, 'name') and application.name:
            try:
                name = application.name.split('.')[-1].replace('_', '-')
            except IndexError:
                raise Exception('No application name is defined.')

            return name

    @staticmethod
    def item_site(application):
        """12-10-2017: The method: "item_site", is part of class: "Item".

        The application is defined as a site. Get the name of the site.

        Returns:
            str: Clean name of the site.

        """
        if hasattr(application, 'site') and application.site:
            return application.site

    @staticmethod
    def item_verbose(application):
        """12-10-2017: The method: "item_verbose", is part of class: "Item".

        The application may have a "Programatic" name definition. By defining a verbose name a plural form or
        general immproved human readable name is defined.

        Returns:
            str: A human readable name or correct plural.

        """
        if hasattr(application, 'verbose_name') and application.verbose_name:
            return application.verbose_name

    @staticmethod
    def item_glyphicon(application):
        """12-10-2017: The method: "item_glyphicon", is part of class: "Item".

        Within the navbar a glyphicon can be additionally given. As defined by bootstrap.

        Returns:
            str: The name of the glyphicon.

        """
        if hasattr(application, 'glyphicon') and application.glyphicon:
            return application.glyphicon


class Labels(object):
    """: The class: "Labels", is part of module: "packages".

    Produce a list of item objects that a defiined as a Label.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.


    """

    def __init__(self):
        """12-10-2017: The method: "__init__", is part of class: "Labels".

        A constructor method for the Labels class. This item is part of a factory pattern. Eventually this list
        of objects is called and marked-up via the Django Template Language.

        Args:
            label (list) : List of Item objects.

        Returns:
            object: Object(Labels) A object containing a list of Item objects.

        """
        self.labels = []

    def process(self):
        """12-10-2017: The method: "process", is part of class: "Labels".

        Load the list of application(settings.py). Filter the application that are required.

        Returns:
            list: Add object(Item) to the list labels.

        """
        for application in apps.get_app_configs():
            if hasattr(application, 'registered') and application.registered:
                label = Item(application)

                self.labels.append(label)

        return reversed(self.labels)


class Sites(object):
    """: The class: "Sites", is part of module: "packages".

    Produce a list of item objects that a defiined as a Site.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.


    """

    def __init__(self):
        """12-10-2017: The method: "__init__", is part of class: "Sites".

        A constructor method for the Sites class. This item is part of a factory pattern. Eventually this list
        of objects is called and marked-up via the Django Template Language.

        Args:
            sites (list) : List of Item objects.

        Returns:
            object: Object(Sites) A object containing a list of Item objects.

        """
        self.sites = []

    def process(self):
        """12-10-2017: The method: "process", is part of class: "Sites".

        Load the list of application(settings.py). Filter the sites that are required.

        Returns:
            list: Add object(Item) to the list sites.

        """
        for application in apps.get_app_configs():
            if hasattr(application, 'site') and application.site:
                site = Item(application)

                self.sites.append(site)

        return self.sites
