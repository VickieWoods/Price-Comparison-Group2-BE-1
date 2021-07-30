from django.conf.urls import include
#from django.contrib import admin
from django.urls import include, path
from blog import views
from .views import comments
from . import views



urlpatterns = [
    path('', views.home, name="index"),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', views.comment_add, name='comments'),

]