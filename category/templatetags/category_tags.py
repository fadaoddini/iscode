from django import template

from category.models import Category

register = template.Library()


@register.simple_tag
def get_category():
    category = Category.objects.filter(status=True).exclude(parent=None).all()
    return category