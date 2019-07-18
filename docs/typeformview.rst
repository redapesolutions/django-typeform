============
TypeformView
============

The ``TypeformView`` replaces the ``FormView`` class and is the default view
for typeforms.

Upon get requests it displays the typeform using the ``template_name`` property
just like a ``FormView``. Upon completion of the typeform the rendered
typeform posts the typeform's unique id to the view.

``TypeformView`` intercepts this post request, uses the Typeform Results
API and retrieves the answers the user has just entered. These answers are
encoded as a ``QueryDict`` and forwarded for form processing.

This way the use of ``TypeformView`` becomes transparent for Django.

See this example, taken from ``urls.py``:

.. code-block:: python

    from django.urls import path
    from django_typeform.views import TypeformView

    from .forms import MyTypeForm

    urlpatterns = [
        ...,
        path('my-typeform/', TypeformView.as_view(
            form_class=MyTypeForm,
            template_name='mytypeform.html',
        )),
        ...,
    ]

where a simple template might look like this (``mytypeform.html``):

.. code-block:: html

    {% extends 'base.html' %}
    {% block content %}
    <form method="post">
      {% include form with height='100vh' %}
    </form>
    {% endblock %}
