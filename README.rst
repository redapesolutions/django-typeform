=============================
Django Typeform
=============================

.. image:: https://badge.fury.io/py/django-typeform.svg
    :target: https://badge.fury.io/py/django-typeform

.. image:: https://travis-ci.org/redapesolutions/django-typeform.svg?branch=master
    :target: https://travis-ci.org/redapesolutions/django-typeform

.. image:: https://codecov.io/gh/redapesolutions/django-typeform/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/redapesolutions/django-typeform


A Typeform integration for Django

Documentation
-------------

The full documentation is at https://django-typeform.readthedocs.io.

Quickstart
----------

Install Django Typeform::

    pip install django-typeform

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_typeform.apps.DjangoTypeformConfig',
        ...
    )

Add Django Typeform's static files to your template:

.. code-block:: html

    <script src="{% static 'django_typeform/embed.js' %}"></script>

Usage:

.. code-block:: html

    {% load django_typeform %}
    <html>
        <body>
            <div class="my-typeform"></div>
            <script src="{% static 'django_typeform/embed.js' %}"></script>
            {% typeforms_embed 'https://xxxx.typeform.com/to/xxxxxx' '.my-typeform' '{"hideHeaders": true, "hideFooter": true}' %}
        </body>
    </html>

Features
--------

* Embed SDK Support
