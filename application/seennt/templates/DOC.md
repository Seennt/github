### Template namespacing
 
Django will choose the first template it finds whose name matches, and if you had a template with
the same name in a different application, Django would be unable to distinguish between them.
Therefor:

    appname/templates/appname

### Template tags
In older versions(<1.10), you had to use {% load static from staticfiles %} in your template to serve files from 
the storage defined in STATICFILES_STORAGE. This is no longer required.