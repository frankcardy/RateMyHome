from django.contrib import admin

# Register your models here.
from .models import Home, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('home', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['comment', 'pub_date']
    search_fields = ['comment']

admin.site.register(Home)
admin.site.register(Review, ReviewAdmin)
