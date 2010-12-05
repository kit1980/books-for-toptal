from django.views.generic.simple import direct_to_template

from book_reviews.models import Review, Category

def home(request):
    return direct_to_template(
        request,
        template='book_reviews/home.html')
