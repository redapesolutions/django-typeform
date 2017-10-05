"""Django Typeform template tags."""
import json

from django import template


register = template.Library()


@register.inclusion_tag('django_typeform/typeform_embed.html')
def typeforms_embed(url, selector, options={}, mode='widget'):
    """Embed a typeforms form.

    Parameters
    ----------
    url : str
        Typeform share url.
    selector : str
        CSS selector to place typeform into.
    options : dict, str
        Accepts a dictionary or JSON as string.
        Options passed into the JS make function.
        see https://developer.typeform.com/embed/modes/ for values.

    """
    if isinstance(options, str):
        # Loads to verify valid JSON is valid.
        options = json.loads(options)
    return {
        'url': url,
        'selector': selector,
        'options': json.dumps(options),
        'mode': mode
    }
