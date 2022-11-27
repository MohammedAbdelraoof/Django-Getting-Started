from django.urls import path

from . import views

urlpatterns = [
    path('', views.productsList, name="products"),
    path('/<int:id>', views.productDetails, name="detail"),
    path('/register', views.userRegister, name="register")
]