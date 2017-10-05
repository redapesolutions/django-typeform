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

Add Django Typeform's URL patterns:

.. code-block:: python

    from django_typeform import urls as django_typeform_urls


    urlpatterns = [
        ...
        url(r'^', include(django_typeform_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
