from django.contrib import admin
from products.models import Product #???
from .models import Comment
from blog import models #Required to register model

# Register your models here.

admin.site.register(Product)
admin.site.register(Comment)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_date')
    list_filter = ('created_date')
    search_fields = ('author', 'text')
    actions = ['approve_comments']