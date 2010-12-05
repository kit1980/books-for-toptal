from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^rpx-response/$', 'django_rpx.views.rpx_response'),
    (r'^logout/$', 'book_reviews.views.logout_view'),


    (r'^/?$', 'book_reviews.views.home'),
# (r'^category/([\w]+)/$', 'book_reviews.views.category_detail'),
    (r'^review/([\d]+)/$', 'book_reviews.views.review_detail'),


    (r'^admin/', include(admin.site.urls)),
)
