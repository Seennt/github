# -*- coding: utf-8 -*-
""" Module: models as part of: collect

    Created by: Reinier on 22-10-2017. A model is the single, definitive source of information about your data.
    It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a
    single database table.

    TODO:
        - Class header: Callback
        - Class header: Errback
        - Class header: Let host, origin & referer depend on URL

"""
from django.db import models


class Header(models.Model):
    """: The class: "Header", is part of module: "models".

    A browser header. To use a header create a dict of it. the field names are dict-keys. and the loaded field values
    are the dict-values. excluded field: name.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.

    """
    #: name(str): Header meant for. E.g. JSON-header.
    name = models.CharField(default='', max_length=100)

    #: accept(CharField):
    accept = models.CharField(default='application/json, text/javascript, */*', max_length=64)

    #: accept_encoding(CharField):
    accept_encoding = models.CharField(default='gzip, deflate, br', max_length=64)

    #: accept_language(CharField):
    accept_language = models.CharField(default='en-US,en;q=0.8,nl;q=0.6', max_length=64)

    #: connection(CharField):
    connection = models.CharField(default='keep-alive', max_length=64)

    #: content_length(IntegerField):
    content_length = models.IntegerField(default=224)

    #: content_type(CharField):
    content_type = models.CharField(default='application/x-www-form-urlencoded', max_length=64)

    #: host(CharField): E.g. www.aex.nl
    host = models.CharField(default='/', max_length=200)

    #: origin(CharField): E.g. https://www.aex.nl
    origin = models.CharField(default='/', max_length=200)

    #: referer(CharField): E.g. https://www.aex.nl/koersen/aandelen-amsterdam
    referer = models.CharField(default='/', max_length=200)

    #: user_agent(CharField):
    user_agent = models.CharField(
        default='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        max_length=200
    )

    #: x_Requested_with(CharField):
    x_Requested_with = models.CharField(default='XMLHttpRequest', max_length=200)

    def __str__(self):
        """28-10-2017: The method: "__str__(self):", is part of class: "Header".

        Provide a human readable name for each header. It is part of a the dropdown list which is displayed in on the
        admin page.

        Returns:
            str: Name of header.

        """
        return self.name


class Config(models.Model):
    """: The class: "Config", is part of module: "models".

    All configuration settings required by: collect.robot.

    """
    #: name(CharField): Topic find by the robot.
    name = models.CharField(max_length=64)

    #: method(str): E.g. POST or GET.
    method = models.CharField(default='GET', max_length=16)

    #: callback(str):
    # callback = ''

    #: header(ForeignKey): Select a request header. E.g. JSON, HTML, etc.
    header = models.ForeignKey(Header, on_delete=models.CASCADE)

    #: encoding(str):
    encoding = models.CharField(default='', max_length=16)

    #: priority(IntegerField):
    priority = models.IntegerField(default=0)

    #: dont_filter(BooleanField):
    dont_filter = models.BooleanField(default=False)

    #: errback(str):
    # errback = ''

    class Meta:
        #: verbose_name(str): The name to display on the admin page.
        verbose_name = 'Configuration'


class Url(models.Model):
    """: The class: "Url", is part of module: "models".

    Start a robot on a specific location on the web. Define each location here as an URL.

    """
    #: url(ForeignKey): A starting point for finding content.
    url = models.ForeignKey(Config, on_delete=models.CASCADE)

    #: address(CharField): A valid web-address(URL)
    address = models.CharField(default='', max_length=200)


class Selector(models.Model):
    """: The class: "Selector", is part of module: "models".

    The expression to extract the data from the HTML body.

    """
    #: expression(ForeignKey): A Xpath of CSS expression.
    expression = models.ForeignKey(Config, on_delete=models.CASCADE)

    #: processor(CharField): A process before... E.g. Time conversion.
    processor = models.CharField(default='', max_length=200)


class FormData(models.Model):
    """: The class: "FormData", is part of module: "models".

    Required form-data to make a correct request.

    """
    #: form(ForeignKey): A starting point for finding content.
    form = models.ForeignKey(Config, on_delete=models.CASCADE)

    #: form_data(CharField): Form field required for html request.
    form_data = models.CharField(default='', max_length=64)


class Meta(models.Model):
    """: The class: "Meta", is part of module: "models".

    Meta request data.

    """
    #: meta(ForeignKey): A starting point for finding content.
    meta = models.ForeignKey(Config, on_delete=models.CASCADE)

    #: meta_data(CharField): Meta request data field.
    meta_data = models.CharField(default='', max_length=64)


class Cookie(models.Model):
    """: The class: "Cookies", is part of module: "models".

    Cookie data to fulfill a data request.

    """
    #: meta(ForeignKey): A starting point for finding content.
    cookie = models.ForeignKey(Config, on_delete=models.CASCADE)

    #: meta_data(CharField): Meta request data field.
    cookie_data = models.CharField(default='', max_length=64)


class Flags(models.Model):
    """: The class: "Flags", is part of module: "models".

    Flags sent to the request, can be used for logging or similar purposes.

    """
    #: meta(ForeignKey): A starting point for finding content.
    flag = models.ForeignKey(Config, on_delete=models.CASCADE)

    #: flag_data(str):
    flag_data = models.CharField(default='', max_length=64)
