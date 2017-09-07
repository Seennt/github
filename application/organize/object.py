# -*- coding: utf-8 -*-
""" Module: data as part of: organize

    Created by: Reinier on 16-8-2017. Collected data comes in a variety of formats. For re-usability data organisation
    is a must. Based on media-type a file naming format is defined.

    Examples:
        Should be defined in a later state.

    TODO:
        - Use TODO comments for code that is temporary, a short-term solution, or good-enough but not perfect.

"""
import glob
import os


class Data(object):
    """: The class: "Data", is part of module: "structure".

    Provide a class description here. A good explanation of a class provides a higher readability of the code.

    Note:
        Do not include the `self` parameter in the ``Args`` section.
        The __init__ method args are defined at class level.
        Class attributes, variables owned by the class itself. All values of class attributes are the same
        for each Instance.

    Args:
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


class Folder(Data):
    """: The class: "Folder", is part of module: "data".

    Provide a class description here. A good explanation of a class provides a higher readability of the code.

    Note:
        Do not include the `self` parameter in the ``Args`` section.
        The __init__ method args are defined at class level.
        Class attributes, variables owned by the class itself. All values of class attributes are the same
        for each Instance.

    Args:
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

    def sub_folder(self):
        pass

    def absolute_path(self):
        return os.path.realpath('')


class File(Data):
    """: The class: "File", is part of module: "data".

    Provide a class description here. A good explanation of a class provides a higher readability of the code.

    Note:
        Do not include the `self` parameter in the ``Args`` section.
        The __init__ method args are defined at class level.
        Class attributes, variables owned by the class itself. All values of class attributes are the same
        for each Instance.

    Args:
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

    def file_name(self):
        pass

    def new_file_name(self):
        pass

    def file_size(self, file):
        if os.stat(file).st_size > 6000:
            return os.stat(file).st_size

    def minimal_file_size(self):
        pass

    def exception_file(self):
        pass

    def other_file(self):
        pass

    def file_type(self):
        pass


class Pattern(object):
    """: The class: "Pattern", is part of module: "data".

    Op basis van het media type(foto, muziek, film, serie, etc.) word gekeken naar de naam van het bestand.
    Als er in de bestandsnaam een bepaald patroon herkend word dit patroon geretourneerd. De bestandsnaam bevat
    ook de titel van het bestand, de titel is afhankelijk van het type media.

    Note:
        Do not include the `self` parameter in the ``Args`` section.
        The __init__ method args are defined at class level.
        Class attributes, variables owned by the class itself. All values of class attributes are the same
        for each Instance.

    Args:
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

    def title(self, options=None):
        """16-8-2017: The method: "title", is part of class: "Pattern".

        A file name isn't always written clean. I.e. "The girlfriend experience" should be "The.girlfriend.experience".

        Args:
            options (list): Description

        Returns:
            str: Description.

        """
        if options is not None:
            self.options = options

        #: docstring_variable(type): Description.
        docstring_variable = self.argument

        return docstring_variable

    def predefined_name_pattern(self, options=None):
        """16-8-2017: The method: "predefined_name_pattern", is part of class: "Pattern".

        - Music: <<Artist>> <<Albumname>> <tracknumber>_<Title>
        - Pictures: ???
        - Series: <<Seriename>> <<Season number(Season_##)>> <Seriename>_<SerieID(S##E##)>
        - Movies:
        - Administration: ??

        Args:
            options (list): Description

        Returns:
            str: Description.

        """
        if options is not None:
            self.options = options

        #: docstring_variable(type): Description.
        docstring_variable = self.argument

        return docstring_variable


class Generate(object):
    """: The class: "DataList", is part of module: "data".

    Load a list with files and folders without any criteria. Based on this list a new list with data objects
    (file, folders, etc.) is generated. Via a factory pattern. In this way files and folders can be altered without
    actually loading the data.

    Note:
        Do not include the `self` parameter in the ``Args`` section.
        The __init__ method args are defined at class level.
        Class attributes, variables owned by the class itself. All values of class attributes are the same
        for each Instance.

    Args:
        arguments (list) : A list of arguments meant for the whole class.
        dictionary (dict) : A dict of value and keys meant for the whole class.
        options (list) : A default optional argument list meant for methods.

    Raises:
        Explain exceptions that are raised during execution. I.e. ValueError.
    """
    #: start_path(str): The variable: "start path" holds the path where the data is stored temporary and raw.
    start_path = ''
    #: final_path(str): The variable: "final path" contains the path where eventually the data will be saved.
    final_path = ''

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.options = []
        self.dictionary = kwargs
        self.argument = args

    def select(self, options=None):
        """2-8-2017: The method: "select", is part of class: "Manager".

        From the default location look for files and directories. Check if it is a file or a directory.
        If it is a directory then go inside. Locate the file and check the filename(if it contains a pattern like
        S##E##. Verify the file size. If all legit than add to list for renaming.

        Args:
            options (list): Select extension list I.e. Music, Photo, Movies, etc.

        Returns:
            list: A list with files larger then 6Mb. Holiding there absolute path.

        """
        if options is not None:
            self.options = options

            #: files(list): This list contains the required extensions.
            files = self.dictionary[self.options]

            select = [glob.glob(file) for file in files]

            return [os.path.realpath(file) for file in select]
        else:
            return 'No extension selection has bin made.'
