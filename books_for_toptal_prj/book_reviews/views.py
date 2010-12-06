from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template

from book_reviews.models import Review, Category

def home(request):
    return list_detail.object_list(
        request,
        queryset=Review.objects.all(),
        extra_context={'sorting': 'top'})

def home_new(request):
    return list_detail.object_list(
        request,
        queryset=Review.objects.all(),
        extra_context={'sorting': 'new'})

def logout_view(request):
    logout(request)
    return redirect('book_reviews.views.home')

def review_detail(request, review_id):
    return list_detail.object_detail(
        request, 
        queryset = Review.objects.all(),
        object_id=review_id,
    )

def review_list(request, category_slug, sorting):
    category = get_object_or_404(Category, slug=category_slug)
    if sorting != "new":
        sorting = "top"

    return list_detail.object_list(
        request,
        queryset=category.review_set.all(),
        extra_context={'category': category, 'sorting': sorting})
