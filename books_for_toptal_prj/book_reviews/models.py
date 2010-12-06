from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

    @models.permalink      
    def get_absolute_url(self): 
        return ('book_reviews.views.review_list', [self.slug, 'top']) 


class Review(models.Model):
    user = models.ForeignKey(User)
    added = models.DateTimeField('added', auto_now_add=True)
    category = models.ForeignKey(Category)
    book_author = models.CharField(max_length=255)
    book_title = models.CharField(max_length=255)
    book_cover = models.ImageField(upload_to='covers/%Y/%m/%d', blank=True)
    text = models.TextField()

    def __unicode__(self):
        return u'%s. %s (user %s)' % (self.book_author, self.book_title, self.user.id)

    # @property
    # def rating(self):
    #     print Votes.objects.filter(review=self).aggregate(models.Sum('rating'))

    @models.permalink      
    def get_absolute_url(self): 
        return ('book_reviews.views.review_detail', [self.id]) 


class Vote(models.Model):
    user = models.ForeignKey(User)
    review = models.ForeignKey(Review)
    rating = models.IntegerField()

    class Meta:
        unique_together = ("user", "review")
 

