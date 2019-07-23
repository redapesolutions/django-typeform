from django.forms import Form
from django.http import QueryDict
from django.template import Context
from django.test import SimpleTestCase

from django_typeform.forms import TypeformMixin


class MyForm(TypeformMixin, Form):
    typeform_url='https://whatever.typeform.com/to/xxxxxx'

    def typeform_to_query_dict(self, typeformuid):
        return QueryDict()   # Set actual response query to nop

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
