from django import template
from shop.models import *

register = template.Library()


@register.inclusion_tag('shop/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}
