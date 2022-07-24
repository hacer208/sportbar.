from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('product/<int:id>/',views.product_detail,name="product_detail"),
    path('basket/',views.basket,name="basket"),
    path('<slug:slug>/',views.home,name="category"),
]
