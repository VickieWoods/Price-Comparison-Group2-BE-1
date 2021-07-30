from django.apps import AppConfig
from products.models import Product
from .models import Comment


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
