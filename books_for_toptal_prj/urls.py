from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^rpx-response/$', 'django_rpx.views.rpx_response'),
    (r'^logout/$', 'book_reviews.views.logout_view'),

    (r'^/?$', 'book_reviews.views.home'),
    (r'^new/?$', 'book_reviews.views.home_new'),

    (r'^review/([\d]+)/$', 'book_reviews.views.review_detail'),
    (r'^new_review/$', 'book_reviews.views.new_review'),

    (r'^category/([-\w]+)/(top|new)/$', 'book_reviews.views.review_list'),

    (r'^admin/', include(admin.site.urls)),
)
