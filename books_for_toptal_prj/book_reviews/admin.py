from django.conf import settings
from django.contrib import admin

from book_reviews.models import Review, Category, Vote

class ReviewAdmin(admin.ModelAdmin):
    pass
admin.site.register(Review, ReviewAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Category, CategoryAdmin)

class VoteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Vote, VoteAdmin)
