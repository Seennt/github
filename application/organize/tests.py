""" Module: views as part of: todo_list

    Created by: Reinier on 18-10-2017.

    Examples:
        self.assertEqual(a, b)	                  # a == b
        self.assertNotEqual(a, b)	              # a != b
        self.assertTrue(x)	                      # bool(x) is True
        self.assertFalse(x)	                      # bool(x) is False
        self.assertIs(a, b)	                      # a is b
        self.assertIsNot(a, b)                    # a is not b
        self.assertIsNone(x)	                  # x is None
        self.assertIsNotNone(x)	                  # x is not None
        self.assertIn(a, b)	                      # a in b
        self.assertNotIn(a, b)	                  # a not in b
        self.assertIsInstance(a, b)	              # isinstance(a, b)
        self.assertNotIsInstance(a, b)	          # not isinstance(a, b)

    TODO:
        - Firt impression.

"""
from django.test import TestCase, Client
from application.organize import content
# Create your tests here.


class TestOrganize(TestCase):
    """: The class: "TestOrganisation", is part of module: "tests".

    Test a part of software.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.

    Raises:
        Explain exceptions that are raised during execution. I.e. ValueError.

    """
    def setUp(self):
        """
        Method called to prepare the test fixture. This is called immediately before calling the test method;

        create a dummy instance of a django model, use django testing tools I.e. Client(), But  also general UnitTest
        preparations are applicable, As it is an inheritance of the unittest method.
        """
        pass

    def test_generate_select(self):
        declared_extensions = {'Movies': ['.avi', '.mp4', '.mkv'], 'Music': ['.mp3']}
        media = 'Movies'

        media_list = content.Generate(**declared_extensions)

        media_list.temporary_location = 'K:\DOWNLOAD\TRANSMISSION\COMPLETE\MOVIES'
        media_list.final_location = ''

        select = media_list.select(options=media)
        print(select)
        self.assertIsNotNone(select, 'This list contains a none empty list.')

# Execute: python manage.py test application.organize
