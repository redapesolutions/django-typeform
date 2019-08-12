# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import include, url
from django_typeform.views import TypeformView
from tests.test_forms import MyForm


urlpatterns = [
    url(r'^testform/', TypeformView.as_view(
        template_name='typeform_test.html',
        form_class=MyForm,
        success_url='/yeah/',
    ))
]
