# -*- coding: utf-8 -*-
""" Module: manager as part of: utility

    Created by: Reinier on 13-11-2017. Task pattern for executing utilities.

    Celery starts a command. This command is configured by means of the defined configuration edited on the admin-page.
    When the configured command is loaded it will be executed. A given result will then be stored a defined in
    the store method.

    TODO:
        - First impression.

"""
REGISTER_CLASS = []


def registered_class(cls):
    """13-11-2017: A class register function to register classes.

        Register all utilities automatically. No manual listing of subclasses elsewhere. E.g. settings.py.

        Args:
             cls (object): Object to register.

    Returns:
        object: Description.

    """
    REGISTER_CLASS.append(cls)
    return cls


class Utility(object):
    """: The class: "Utility", is part of module: "manager".

    Utility interface.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.

    Raises:
        Explain exceptions that are raised during execution. I.e. ValueError.

    """

    def __init__(self, *args, **kwargs):
        """13-11-2017: The method: "__init__", The constructor of class: "Utility".

        A constructor method for the Item class. This item is part of a factory pattern.

        Args:
            arguments (list) : A list of arguments meant for the whole class.
            dictionary (dict) : A dict of value and keys meant for the whole class.

        Attributes:
            arguments (list) : A list of arguments meant for the whole class.
            dictionary (dict) : A dict of value and keys meant for the whole class.

        """
        self.argument = args
        self.dictionary = kwargs
        self.load = None
        self.utility = None
        self.store = None
        self.display = None

    def run(self):
        """13-11-2017: The method: "run", is part of class: "Utility".

        Call the required utility.

        Returns:
            object: Utiltity collect.

        """
        try:
            if self.validate():
                self.load = self.load_utility()
                self.utility = self.execute()

            if isinstance(self.utility, object):
                if self.store:
                    self.store_utility()

                if self.display:
                    self.display_utility()

            return self.utility

        except NotImplementedError:
            raise Exception('Could not run the given configuration, verify if configuration is correctly loaded.')

    def execute(self):
        """15-11-2017: The method: "execute", is part of class: "Utility".

        Fulfill all post-conditions. and execute all steps from of a roadmap.

        Returns:
            object: Description.

        """
        self.store = False

        self.display = False

        raise NotImplementedError

    def validate(self):
        """15-11-2017: The method: "validate", is part of class: "Utility".

        Validate the utility initialization. Verify all pre-conditions.

        Returns:
            bool: Return a validated data set.

        """
        raise NotImplementedError

    def configure(self):
        """13-11-2017: The method: "configure", is part of class: "Utility".

        Load the configuration  and prepare to run the required utility.

        Returns:
            object: Description.

        """
        raise NotImplementedError

    def save(self):
        """13-11-2017: The method: "save", is part of class: "Utility".

        Store the returned data.

        Returns:
            object: By default save the utility feedback in a JSON file.

        """
        try:
            return self.utility
        except ValueError:
            raise ValueError

    def display(self):
        """13-11-2017: The method: "display", is part of class: "Utility".

        Show the returned data.

        Returns:
            dict: Provide a dict that can be sent to the Django Template system.

        """
        try:
            return self.utility
        except ValueError:
            raise ValueError
