# -*- coding: utf-8
"""Define TypeformView."""

from django.views import View
from django.views.generic.edit import FormMixin
from django.views.generic.base import TemplateResponseMixin


class BaseTypeformView(FormMixin, View):
    """
    Render a typeform_id on GET and retrieve typeform_id results
    and process them it on POST.
    """
    typeform_url = None

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: get typeform_id results from typeform_id API,
        instantiate a form instance with the retrieved input and then 
        check if it's valid.
        """

        if 'typeformuid' in request.POST:
            request.POST = self.form_class().typeform_to_query_dict(request.POST.get('typeformuid'))
            return self.post(request, *args, **kwargs)
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class TypeformView(TemplateResponseMixin, BaseTypeformView):
    """A view for displaying a typeform_id and rendering a template response."""
