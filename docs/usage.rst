=====
Usage
=====

To use Django Typeform in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_typeform.apps.DjangoTypeformConfig',
        ...
    )

Make sure your TEMPLATE OPTIONS' context_processors include

.. code-block:: python

    TEMPLATES = [
        {
            ...
            'OPTIONS': {
                'context_processors': [
                    ...
                    'django.template.context_processors.request',
                    ...
                ]
            }
        },
    ]

The ``typeform_embed`` template tag includes a ``<div>`` at its position. It carries
a class


Example:

.. code-block:: html

    {% load django_typeform %}
    <html>
        <body>
             {% typeforms_embed 'https://xxxx.typeform.com/to/xxxxxx' '.my-typeform' '{"hideHeaders": true, "hideFooter": true}' %}
        </body>
    </html>

