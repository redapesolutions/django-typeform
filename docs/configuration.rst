=============
Configuration
=============

``django_typeform`` interacts with the Typeform Responses API. To use the
API you need to get a **Personal token** from typeform.


TYPEFORM_TOKEN
..............

The ``TYPEFORM_TOKEN`` setting is **required**. It carries the
personal token of the typeform account. Example:

.. code-block:: python

    TYPEFORM_TOKEN = 'heregoesthereallylongtokenstringgiventoyoubytypeform'

Without the token the Responses API will not work and type ``TypeformMixin`` will
not be able to retrieve responses. The template tags are unaffected.


