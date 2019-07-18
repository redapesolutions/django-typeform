=============
TypeformMixin
=============

To process a typeform in Django just the way you would process a Django form,
use the ``TypeformMixin``. It requires the typeform to be mirrored by a corresponding
Django form, question by question, but can also contain processing logic.
To turn Typeform features on for a Django form just use the Mixin and specify
the ``typeform_url``:

.. code-block:: python

    from django_typeforms.forms import TypeformMixin

    from forms import MyForm

    class MyTypeForm(TypeformMixin, MyForm)
        typeform_url = 'https://xxxx.typeform.com/to/xxxxxx'

``MyTypeForm`` will be a fully fledged Django form and at the same
time be linked to the Typeform with given url.

For this link to work, the ``Question reference`` for each Typeform
question must be set to the matching Django field name, e.g. ``first_name`` for a
field ``first_name = forms.CharField(max_length=40, blank=True)``. **This requires editiing
all questions of a typeform and as Typeform warns might break
other integrations.**

Additionally, the typeform needs a **hidden field** "typeformuid" which
the ``TypeformMixin`` uses to identify the relevant answer sent to the
Typeform servers. Hidden fields currently are only available to
users of the Typeform PRO and PRO+ plans.

Rendering a typeform
--------------------

Once, a form is turned into a typeform using the mixin, it still can
used and rendered as a Django form using, e.g., ``{{ form }}`` or any
other of your preferred rendering methods.

Additionally, it can be rendered as a typeform using include:

.. code-block:: html

    <form method="post">
      {% include form with mode='popup' %}
    </form>

This will render a hidden input field with a unique id passed to the
typeform's hidden ``typeformuid`` field. Upon completion of
the typeform the above HTML form is posted to the server and
the server can retrieve the answers given by querying the response
with the unique id.

Additional context can be given to the typeform using the ``with`` clause.

Currently, valid context parameters are:

mode
....
``mode`` (default: None) describes the emed mede to be used: ``None`` or ``widget``
for a widget. In widget mode the additional parameter ``height`` is
needed for proper display. Example:

.. code-block:: html

    <form method="post">
      {% include form with mode='widget' height='100vh' %}
    </form>

Other values of ``mode`` can be ``popup``, ``drawer_left``, or
``drawer_right`` which are the three modes for typeform popup modes.


Form validation
---------------

Both Django and Typeform provide form validation. This is prone for conflicts
since both validations need not agree. When turning a Django form into a typeform
we recommend to leave out any validation on the Django side, since for now
there is no way of returning validation errors to typeform.
