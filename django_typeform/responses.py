# -*- coding: utf-8
"""
Implement the response API of typeform_id.

The class TypeformResponse reads JSON objects as described on the typeform_id developer web site:
https://developer.typeform.com/
"""

import json
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from dateutil.parser import parse
from django.conf import settings
from django.http import QueryDict

TYPEFORM_SERVER = getattr(settings, 'TYPEFORM_SERVER', 'https://api.typeform.com/')
if TYPEFORM_SERVER[-1] != '/':  #  add trailing slash if missing
    TYPEFORM_SERVER += '/'
TYPEFORM_FORM = getattr(settings, 'TYPEFORM_FORM', None)
TYPEFORM_TOKEN = getattr(settings, 'TYPEFORM_TOKEN', "")
TYPEFORM_CHOICES = getattr(settings, 'TYPEFORM_CHOICES', {})


class TypeformResponses(object):
    """
    Retrieve typeform response answers and convert them to Django form compatible
    formats.

    "Decode" is a dictionary of functions to decode results returned as json objects by
    the typeform response api. Currently it supports choice fields and date fields.
    Additional fields to be added.
    
    All types not listed in decode will follow the rule lambda x: x[answer['type']],
    i.e. the property named after the answer type contains the result.

    Since Django separates representation and answers for choice fields, answers
    will have to converted back to representationd in _to_choice_field.
    """
    decode = {
        'choice': lambda x: x['choice']['label'] if x['choice'] else None,
        'date': lambda x: parse[x['date']],
    }
    form = None

    def __init__(self, *args, **kwargs):
        self.form_id = kwargs.pop('form', TYPEFORM_FORM)
        super().__init__(*args, **kwargs)


    def get(self, parameters, form_id = None):
        """
        Read typeform_id results from server
        :param form_id: Typeform form id for form to read (overwrites the form_id given on object initialization)
        :type parameters: dict
        """
        if form_id is None:
            if self.form_id:
                form_id = self.form_id
            else:
                raise ValueError('No form_id specified for typeform_id response api')

        url = "{}forms/{}/responses".format(TYPEFORM_SERVER, form_id)
        if parameters:
            url += "?" + urlencode(parameters)

        request = Request(url)
        request.add_header('authorization', 'bearer {}'.format(TYPEFORM_TOKEN))

        results = urlopen(request)
        if results.status == 200:       # OK
            data = json.loads(results.read())
        else:
            raise HTTPError('Error reading form typeform_id response api: {} {}'
                            .format(results.status, results.reason))

        return data

    def _to_choice_field(self, value, form_id, form_field):
        """
        Convert choice field value to Django FormField representation in
        two-step process. First try form_field.choices attribute to find
        representation. Secondly, try TYPEFORM_CHOICES setting which contains
        a dictionary for choices attributes for a given typeform id.

        :param value: Returned value from response api
        :param form_id: typeform id
        :param form_field: ChoiceField object
        :return:
        """
        if form_field:
            choices = getattr(form_field, 'choices', [])
            for choice in choices:
                if choice[-1] == value or choice[1] == value:
                    return choice[0]
        if form_id in TYPEFORM_CHOICES:
            for choice in TYPEFORM_CHOICES[form_id]:
                if choice[-1] == value or choice[1] == value:
                    return choice[0]
        return value

    def query_dict(self, result_id, parameters, form_id=None, helper_form=None):
        if form_id is None:
            form_id = self.form_id
        if isinstance(helper_form, type):  # is (new style) class?
            helper_form = helper_form()
        data = self.get(parameters, form_id)
        if 0 <= result_id < data['total_items']:
            answers = data['items'][result_id]

            q_dict= QueryDict(mutable=True)
            for answer in answers.get('answers'):
                field = answer.get('field', {'ref': None}).get('ref', None)
                if field:
                    q_dict[field] = self.decode.get(answer['type'], lambda x: x[answer['type']])(answer)
                    if answer['type'] == 'choice':
                        if helper_form:
                            q_dict[field] = self._to_choice_field(q_dict[field], form_id, 
                                helper_form.fields.get(field, None))
                        else:
                            q_dict[field] = self._to_choice_field(q_dict[field], form_id, None)
            return q_dict
        raise HTTPError('No typeform result supplied from results api')
