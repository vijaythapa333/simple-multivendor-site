from . import views
from django.urls import path



app_name = 'product'


urlpatterns = [
    path('search', views.search, name="search"),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name="product"),
    path('<slug:category_slug>/', views.category, name="category"),
    
]
