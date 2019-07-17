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

