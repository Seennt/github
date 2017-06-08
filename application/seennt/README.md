## Seennt
A  Internet of Things(IoT) application.

#### Application structure
Platform dependent and application dependent.

Meaning:

        system:
            static
            templates
    
        application:
            app_name:
               static:
                ...
               templates:
                app_name

For instance the favicon of a app should be loaded via the application it ain't relevant
for the platform.