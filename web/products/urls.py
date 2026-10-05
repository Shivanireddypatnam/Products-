from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('add_product/', views.create_product, name='add_product'),
    path('update_product/<int:id>/', views.update_product, name='update_product')
]