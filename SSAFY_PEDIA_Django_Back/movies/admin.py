from django.contrib import admin
from .models import Movie, Review, Comment

class MovieAdmin(admin.ModelAdmin):
  list_display = ['pk', 'title']

class ReviewAdmin(admin.ModelAdmin):
  list_display = ['pk', 'title']

class CommentAdmin(admin.ModelAdmin):
  list_display = ['pk', 'content']

# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
