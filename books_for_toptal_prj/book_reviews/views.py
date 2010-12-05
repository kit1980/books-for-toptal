from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template

from book_reviews.models import Review, Category

def home(request):
    return direct_to_template(
        request,
        template='book_reviews/home.html')

def logout_view(request):
    logout(request)
    return redirect('book_reviews.views.home')

def review_detail(request, review_id):
    return list_detail.object_detail(
        request, 
        queryset = Review.objects.all(),
        object_id=review_id,
    )
