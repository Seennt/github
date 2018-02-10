# -*- coding: utf-8 -*-
""" Module: utility as part of: collect

    When a “collect” task is configured in Celery utility collect start execute. The provided collect task will then
    load the corresponding configuration from the database. This configuration is defined by models Config, Url,
    Header, Selector, Cookie, etc.

    When all models are instantiate the configuration needs to be prepared to run. The header to collect data needs
    to be assembled with header- and url- configuration settings, via “create_header_dict” this can be realized.

    Basic settings...

    The URLs are meant for start_requests and for host, origin and referer the last items are part of the header.
    only one URL can be defined as  host, origin or referer

    Selectors, etc...
    
    Examples:
        UtilityName(Utility):

            validate(self): # required
                pass

            execute(self): # required
                pass

            configure(self): # required
                pass

            save(self): # optional
                pass

            display(self) # optional
                pass

        UtilityName.run()

    TODO:
        - Explain basic settings
        - Explain Selectors, etc.
        
"""
from utility.collect import models
from utility.collect.spiders import find
from utility.config import registered_class, Manager


@registered_class
class Collect(Manager):
    """: The class: "Collect", is part of module: "utility".

    Collect utility to collect and find a request given from Celery or Manually(CMD).

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.

    Raises:
        Explain exceptions that are raised during execution. I.e. ValueError.

    """

    def __init__(self, *args, **kwargs):
        """30-10-2017: The method: "__init__", The constructor of class: "Collect".

        A constructor method for the Item class. This item is part of a factory pattern.

        """
        super().__init__(*args, **kwargs)

    def validate(self):
        """17-11-2017: The method: "validate", is part of class: "".

        Preconditions.

        Returns:
            str: Description.

        """
        return True

    @property
    def execute(self):
        """15-11-2017: The method: "execute", is part of class: "Collect".

        Post-conditions to execute the utility Collect.

        Returns:
            object: Command instance.

        """
        # self.load is instantiated via the run command
        if self.load:
            self.store = True

            command_collect = find.Command(**self.load)

            # Command is a Singleton class. command_collect instantiates. Process_collect reloads instance.
            find.process_collect(command_collect)

            return command_collect

        else:
            # NotImplementedError
            return self.load

    def configure(self):
        """30-10-2017: The method: "configure", is part of class: "Collect".

        Load the configuration to find and collect.

        Returns:
            dict: Collect configuration command.

        """
        load_utility = {}

        #: configuration(object): Load the configuration from the database.
        configuration = models.Config.objects.get(id=self.dictionary['id'])

        load_utility['configuration'] = configuration

        load_utility['header'] = self.make_header_dict(configuration.header, configuration.url_set.all())

        load_utility['start_urls'] = [url.address for url in configuration.url_set.all() if not url.host]

        load_utility['selector'] = configuration.selector_set.all()

        load_utility['formdata'] = configuration.formdata_set.all()

        load_utility['cookie'] = configuration.cookie_set.all()

        load_utility['meta'] = configuration.meta_set.all()
        load_utility['flag'] = configuration.flag_set.all()

        return load_utility

    def save(self):
        """30-10-2017: The method: "save", is part of class: "Collect".

        Store the collected data as requested. E.g. JSON, mongoDB, djangoItems, etc. configure a feed export via
        a pipeline.

        Returns:
            str: Description.

        """
        print('Items stored via JsonPipeline.')
        return None

    @staticmethod
    def make_header_dict(header, urls):
        """2-11-2017: The method: "make header dict", is part of class: "Collect".

        Make a header dict based on the URL model and Config model Header model and provided it for the headers
        argument as part of scrapy.request()

        Args:
            urls (list): A list of objects containing URLs.
            header (object): A header object including HTTP fields.

        Returns:
            str: Description.

        """
        #: host_url(str): A website host address.
        host_url = None

        #: header_dict(dict): A complete header request as a dict.
        header_dict = {}

        for url in urls:
            if url.host:
                host_url = url.address

            if url.origin:
                header_dict['origin_url'] = url.address

            if url.referer:
                header_dict['referer_url'] = url.address

        if host_url is not None:
            header_dict[' host_url'] = host_url
        else:
            raise NameError

        #: Add the above fields to a header dict.
        for header_key, header_value in header.__dict__.items():
            header_dict[header_key] = header_value

        return header_dict
