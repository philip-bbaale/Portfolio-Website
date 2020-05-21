from django.contrib import admin
from blog.models import Post, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
   filter_horizontal =('categories',)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)