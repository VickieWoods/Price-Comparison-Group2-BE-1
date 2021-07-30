from django.urls import path
from .import views 
from django.urls import path, include
from .views import index, ebayindex

urlpatterns = [
    path('amazon', views.amazon, name='amazon'),
    path('ebay', views.ebay, name='ebay'),
    path('blog/', include('blog.urls')),
]