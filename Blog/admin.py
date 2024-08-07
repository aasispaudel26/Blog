from django.contrib import admin
from .models import Tag
from.models import Author
from.models import Post

# Register your models here.

# class TagAdmin(admin.ModelAdmin):
#   list_display = ("caption")
  
# class AuthorAdmin(admin.ModelAdmin):
#   list_display = ("first_name","last_name","email_address")
  
class PostAdmin(admin.ModelAdmin):
  list_filter = ("author","tag","date")
  list_display =("title","date","author")
  prepopulated_fields = {"slug": ("title",)}

admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post,PostAdmin)
