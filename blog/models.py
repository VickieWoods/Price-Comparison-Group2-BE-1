from django.db import models
#from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from products.models import Product


# IMPLEMENT THE COMMENT MODELS HEREfrom django.db import models


# Create your models here.
class Comment(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text