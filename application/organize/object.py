# -*- coding: utf-8 -*-
""" Module: data as part of: organize

    Created by: Reinier on 16-8-2017. Collected data comes in a variety of formats. Data should be organized in a
    structured manner to achieve a better usability of available data like movies, series, pictures, documents, etc.
    also known as media-type.

    All gathered data by means of: mail, download, etc. is temporarily saved in a predefined location.
    Data is undefined which means that object-names are raw and relevance isn’t added.

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
    """: The class: "Folder", is part of module: "object".

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
    """: The class: "File", is part of module: "object".

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


class Structure(object):
    """: The class: "Structure", is part of module: "object".

    As an aspect of organizing data gathering information of an object is essential. Information that should be
    gathered is a pattern and title and/or name. If this information can’t be gathered, manual selection via a
    user interface should be possible.

    Raw data can consists of several files, based on the media type a object size criteria is essential. In addition
    supporting file should be kept and can be defined as exception files(subtitles).

    The title and pattern will then be used to create the final location and file of folder object, relevant object.
    I.e. For series a id is given like: S##E## based on it a (sub)folder like: “Season_##” is created.

    A new object name in relation to a predefined name pattern following a naming convention is made.

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

    def title_or_name(self, options=None):
        """16-8-2017: The method: "title_or_name", is part of class: "Structure".

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
        """16-8-2017: The method: "predefined_name_pattern", is part of class: "Structure".

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
    """: The class: "Generate", is part of module: "object".

    From starting point “temporary location” a data-list is generated containing all data items. Data items like
    folders, (sub)folders, files, etc. are registered but not loaded.

    Based on this raw data list each item should then be converted to a corresponding object. Each item contains a
    relative path and a object name. Via a factory pattern. In this way files and folders can be altered without
    actually loading the data.

    Note:
        Do not include the `self` parameter in the ``Args`` section.
        The __init__ method args are defined at class level.
        Class attributes, variables owned by the class itself. All values of class attributes are the same
        for each Instance.

    Args:
        arguments (list) : A list of arguments meant for the whole class.
        dictionary (dict) : The dictionary contains the relevant extension for each media type.
        options (list) : A default optional argument list meant for methods.

    Raises:
        Explain exceptions that are raised during execution. I.e. ValueError.
    """
    #: temporary_location(str): The variable: "temporary location" for undefined and raw data.
    temporary_location = ''
    #: final_location(str): The variable: "final location" contains the path where eventually the data will be saved.
    final_location = ''

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.options = []
        self.dictionary = kwargs
        self.argument = args

    def select(self, options=None):
        """2-8-2017: The method: "select", is part of class: "Generate".

        From the temporary location look for files and directories. Check if it is a file or a directory.
        If it is a directory then go inside. Locate the file and check the filename(if it contains a pattern like
        S##E##. Verify the file size. If all legit than add to list for renaming.

        Via options you can pass a media-type. I.e. Movies. Applicable extension are: ".avi, .mp4, .mkv"

        Args:
            options (list): Select extension list I.e. Music, Photo, Movies, etc.

        Returns:
            list: A list with files larger then 6Mb. Holiding there absolute path.

        """
        if options is not None:
            self.options = options

            #: files(list): This list contains the required extensions.
            files = self.dictionary[self.options]

            return [glob.glob(self.temporary_location + '/**/*' + file, recursive=True) for file in files]
        else:
            return 'No extension selection has bin made.'
