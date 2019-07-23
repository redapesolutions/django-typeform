# -*- coding: utf-8
"""Define TypeformMixin."""
import hashlib

from django.template.loader import render_to_string
from django.utils.crypto import get_random_string

from .responses import TypeformResponses


class TypeformMixin(object):
    """
    Extend a Form class to add Typeform funcitonality.
    """
    typeform_id = None
    typeform_url = None
    typeform_template = 'django_typeform/typeform.html'

    def __init__(self, *args, **kwargs):
        self.typeform_url = kwargs.pop('typeform_url', self.typeform_url)
        if self.typeform_url:
            if self.typeform_url[-1] == '/':  # Skip trailing /
                self.typeform_url = self.typeform_url[:-1]
            self.typeform_id = self.typeform_url.rsplit('/', 1)[-1]  # slug is typeform_id

        return super().__init__(*args, **kwargs)

    def typeform_to_query_dict(self, typeformuid):
        """
        Get repsonse from typeform respopnses api as a query dict suitable
        for POST.
        """
        server = TypeformResponses(form=self.typeform_id)
        result = server.query_dict(0, {
            'query':        typeformuid,
            'page_size':    1,
            'sort':         'submitted_at,desc',
        }, helper_form=self)
        return result

    def get_uid(self, request):
        """Generate unique id for each typeform and session"""
        hash = hashlib.md5(self.typeform_id.encode('utf-8')).hexdigest()
        if hash in request.session:
            return request.session[hash]
        request.session[hash] = get_random_string(31)  # unique id is random
        return request.session[hash]

    def render(self, context):
        """
        Renders the typeform. Allows to use "{% include typeform %}" in templates
        for typeform rendering
        """
        request = context['request']
        context.update({
                'typeformuid':      self.get_uid(request),
                'typeform_url':     self.typeform_url,
            })
        return render_to_string(self.typeform_template, context.flatten())
