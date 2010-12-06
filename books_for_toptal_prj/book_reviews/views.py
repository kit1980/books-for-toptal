from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db import models
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template

from book_reviews.models import Review, Category, Vote

def home(request):
    return list_detail.object_list(
        request,
        queryset=Review.objects.all().annotate(rating=models.Sum('vote__rating')).order_by('-rating', '-added'),
        extra_context={'sorting': 'top'})

def home_new(request):
    return list_detail.object_list(
        request,
        queryset=Review.objects.all().annotate(rating=models.Sum('vote__rating')).order_by('-added'),
        extra_context={'sorting': 'new'})

def logout_view(request):
    logout(request)
    return redirect('book_reviews.views.home')

def review_detail(request, review_id):
    return list_detail.object_detail(
        request, 
        queryset=Review.objects.all().annotate(rating=models.Sum('vote__rating')),
        object_id=review_id,
    )

def review_list(request, category_slug, sorting):
    category = get_object_or_404(Category, slug=category_slug)

    if sorting != "new":
        sorting = "top"
        reviews = category.review_set.annotate(rating=models.Sum('vote__rating')).order_by('-rating', '-added')
    else:
        reviews = category.review_set.order_by('-added')

    return list_detail.object_list(
        request,
        queryset=reviews,
        extra_context={'category': category, 'sorting': sorting})


@login_required
def new_review(request):
    class ReviewForm(ModelForm):
        def __init__(self, user, *args, **kwargs):
            self.user = user
            super(ReviewForm, self).__init__(*args, **kwargs)

        class Meta:
            model = Review
            exclude = ('user',)


    form = ReviewForm(request.user, request.POST or None, request.FILES)

    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.save()

        # upvote newly created review
        vote = Vote()
        vote.user = request.user
        vote.review = review
        vote.rating = +1
        vote.save()

        return redirect(review_detail, review.id)

    return direct_to_template(request, 'book_reviews/review_form.html', {'form': form}) 


# TODO: should be POST
@login_required
def upvote_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    try:
        vote = Vote.objects.get(user=request.user, review=review)
    except Vote.DoesNotExist:
        vote = Vote(user=request.user, review=review)
    vote.rating = 1    
    vote.save()

    return redirect(review_detail, review.id)


# TODO: should be POST
@login_required
def downvote_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    try:
        vote = Vote.objects.get(user=request.user, review=review)
    except Vote.DoesNotExist:
        vote = Vote(user=request.user, review=review)
    vote.rating = -1    
    vote.save()

    return redirect(review_detail, review.id)

    
