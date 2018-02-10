# -*- coding: utf-8 -*-
""" Module: test as part of: collect
    
    Created by: Reinier on 22-11-2017. Testing collect utility.
    
    Example
    
    Attributes

    TODO:
        - First impression.
        
"""
from django.test import TestCase
from utility.collect import models


class TestCollect(TestCase):
    """: The class: "TestCollect", is part of module: "test".

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance. 

    Raises:
        Explain exceptions that are raised during execution. I.e. ValueError.
    
    """
    def setUp(self):
        """22-11-2017: The method: "setUp", is part of class: "TestCollect".
                
        Returns:
            str: Description.
    
        """
        header = {'name': 'quotes.toscrape.com',
                  # 'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp",
                  'accept_encoding': 'gzip, deflate',
                  'accept_language': 'en-US,en;q=0.8,nl;q=0.6',
                  'cache_control': 'max-age=0',
                  'upgrade_insecure_requests': 1,
                  'connection': 'keep-alive',
                  'content_length': None,
                  'content_type': None,
                  'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                ' Chrome/61.0.3163.100 Safari/537.36',
                  'x_Requested_with': None
                  }

        models.Config.objects.create(**header)

        # config = {
        #     'name': 'quotes.toscrape.com',
        #     'method': 'GET',
        #     'header_id': header_instance.header_id,
        #     'encoding': 'utf-8',
        #     'priority': 0,
        #     'dont_filter': False
        # }
        #
        # config_instance = models.Config.objects.create(**config)

    def test_header(self):
        """22-11-2017: The method: "test_header", is part of class: "TestCollect".

        Returns:
            str: Description.

        """
        return models.Header.objects.get(id=1).__dict__
