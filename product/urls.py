from django.contrib import admin
from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('',views.products, name='products'),
    path('dets/<int:pk>/',views.ProductClassBasedDetailView.as_view(), name='product_detail'),
    path('add/', views.AddClassBasedView.as_view(), name='AddProduct'),
    path('update/<int:pk>/', views.UpdateClassBasedView.as_view(), name='UpdateProduct'),
    path('delete/<int:pk>/', views.DeleteClassBasedView.as_view(), name='DeleteProduct'),
    path('mylistings', views.my_listings, name='mylistings'),
]












