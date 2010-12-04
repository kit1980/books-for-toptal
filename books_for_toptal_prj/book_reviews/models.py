from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return '/category/%i/' % self.id


class Review(models.Model):
    user = models.ForeignKey(User)
    added = models.DateTimeField('added', auto_now_add=True)
    category = models.ForeignKey(Category)
    book_author = models.CharField(max_length=255)
    book_title = models.CharField(max_length=255)
    book_cover = ImageField(upload_to='covers/%Y/%m/%d', blank=True)
    text = models.TextField()

    def __unicode__(self):
        return u'%s. %s (user %s)' % (self.book_author, self.book_title, self.user.id)

    # @property
    # def rating(self):



    def get_absolute_url(self):
        return '/review/%i/' % self.id


class Votes(models.Model):
    user =  models.ForeignKey(User)
    review = models.ForeignKey(Review)

