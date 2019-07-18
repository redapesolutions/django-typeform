from django.forms import Form
from django.template import Context

from django_typeform.forms import TypeformMixin
from django.test import SimpleTestCase


class MyForm(TypeformMixin, Form):
    typeform_url='https://whatever.typeform.com/to/xxxxxx'


class TypeformMixinTest(SimpleTestCase):
    def test_mixin(self):
        form = MyForm()
        self.assertEqual(form.typeform_id, 'xxxxxx')

    def test_mixin_rendering(self):
        class Request(object):
            session = {}

        request = Request()
        form = MyForm(typeform_url='https://whatever.typeform.com/to/xxxxxx')

        form.get_uid(Request())
        self.assertFalse(not request.session, 'typeformuid not stored in session')
        form.render(Context({'request': Request()}))
