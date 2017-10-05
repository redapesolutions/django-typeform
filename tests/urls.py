# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_typeform.urls import urlpatterns as django_typeform_urls

urlpatterns = [
    url(r'^', include(django_typeform_urls, namespace='django_typeform')),
]
