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

Add Django Typeform's static files to your template:

.. code-block:: html

    <script src="{% static 'django_typeform/embed.js' %}"></script>

Example:

.. code-block:: html

    {% load django_typeform %}
    <html>
        <body>
            <div class="my-typeform"></div>
            <script src="{% static 'django_typeform/embed.js' %}"></script>
            {% typeforms_embed 'https://xxxx.typeform.com/to/xxxxxx' '.my-typeform' '{"hideHeaders": true, "hideFooter": true}' %}
        </body>
    </html>


... code-block:: html

    {% load django_typeform %}
    <html>
        <body>
            <div id="my-css-selector"></div>
            <script src="{% static 'django_typeform/embed.js' %}"></script>
            {% typeforms_embed 'https://xxxx.typeform.com/to/xxxxxx' '#my-css-selector' options_as_dict_var %}
        </body>
    </html>
