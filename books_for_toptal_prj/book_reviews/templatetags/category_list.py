from django import template
from book_reviews.models import Category

register = template.Library()

@register.inclusion_tag('book_reviews/category_list.html')
def category_list():
    return {'category_list': Category.objects.all()}
