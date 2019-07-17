from django.forms import Form
from django.template import Context

from django_typeform.forms import TypeformMixin
from django.test import SimpleTestCase


class MyForm(TypeformMixin, Form):
    pass

class TypeformMixinTest(SimpleTestCase):
    def test_mixin(self):
        form = MyForm(typeform_url='https://whatever.typeform.com/to/xxxxxx')
        self.assertEqual(form.typeform_id, 'xxxxxx')

