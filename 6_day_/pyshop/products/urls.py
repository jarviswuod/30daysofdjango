from django.urls import path
from . import views

# /
# /products/1/detail
# /products/new/trending
urlpatterns = [
    path('', views.index),
    path('new/', views.new_products)
]
