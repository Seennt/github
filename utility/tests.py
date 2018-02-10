# -*- coding: utf-8 -*-
""" Module: tests as part of: collect
    
    Created by: Reinier on 22-11-2017. Testing collect utility.
    
    Example
    
    Attributes

    TODO:
        - First impression.
        
"""
from django.test import TestCase
from utility.collect import models, compile


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

    @staticmethod
    def separation_line():
        return '\n----------------------------------------------------------------------\n'

    def setUp(self):
        """22-11-2017: The method: "setUp", is part of class: "TestCollect".

        """
        header = {'name': 'quotes.toscrape.com',
                  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp',
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

        models.Header.objects.create(**header)

        config = {
            'name': 'quotes.toscrape.com',
            'method': 'GET',
            'header_id': models.Header.objects.get(name='quotes.toscrape.com').id,
            'encoding': 'utf-8',
            'priority': 0,
            'dont_filter': False
        }

        config_instance = models.Config.objects.create(**config)

        models.Url.objects.create(id=1, url_id=config_instance.id,
                                  address='quotes.toscrape.com', host=True, origin=False, referer=False)
        models.Url.objects.create(id=2, url_id=config_instance.id,
                                  address='http://quotes.toscrape.com/', host=False, origin=True, referer=False)

        models.Selector.objects.create(id=2, selector_id=config_instance.id, selector_key='name',
                                       expression='//title/text()', expression_type='True',
                                       expression_main=True, processor=None)

        # models.FormData.objects.create()
        # models.Cookie.objects.create()
        # models.Tests.objects.create()

        self.config = models.Config.objects.get(name='quotes.toscrape.com')

        self.command_collect = compile.Order(**{'id': self.config.id}).run()

    def test_utility_collect(self):
        """22-11-2017: The method: "test_utility_collect_find_command", is part of class: "TestCollect".

        """
        print(self.separation_line())
        print(self.command_collect.__dict__)
