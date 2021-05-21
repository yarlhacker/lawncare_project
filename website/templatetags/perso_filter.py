from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape
from random import randint

register = template.Library() # fonction d'enregistrement



@register.filter(name='my_filtre_new_name', is_safe=True)
def my_filtre(param):
    param = escape(param)
    return mark_safe(param.upper())


@register.simple_tag(name='random', takes_context=True)
def random(context, begin, end):
   try:
      return randint(int(begin), int(end))
   except ValueError:
      raise template.TemplateSyntaxError('Les arguments doivent nécessairement être des entiers')