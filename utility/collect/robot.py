# -*- coding: utf-8 -*-
""" Module: robot as part of: collect
    
    Created by: Reinier on 28-10-2017.Provide a module description here. A good explanation for a module provides
    a higher readability and will improve implementation.
    
    Examples:
        Should be defined in a later state.
    
    Attributes:
        module_variable(str): Module level variables are documented in the ``Attributes`` section of the
        module docstring.
        
    TODO:
        - Use TODO comments for code that is temporary, a short-term solution, or good-enough but not perfect.
        
"""
module_variable = ''


class Execute(object):
    """: The class: "Execute", is part of module: "robot".

    Provide a class description here. A good explanation of a class provides a higher readability of the code.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.

    Args:
        arguments (list) : A list of arguments meant for the whole class.
        dictionary (dict) : A dict of value and keys meant for the whole class.

    Attributes:
        arguments (list) : A list of arguments meant for the whole class.
        dictionary (dict) : A dict of value and keys meant for the whole class.
        options (list) : A default optional argument list meant for methods.

    Raises:
        Explain exceptions that are raised during execution. I.e. ValueError.
    """

    #: class_variable(str): Description.
    class_variable = ''

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.options = []
        self.dictionary = kwargs
        self.argument = args
