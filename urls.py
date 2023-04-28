from django.urls import path

from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
        #Leave as empty string for base url
	path('', views.Store.as_view(), name="store"),
	path('cart/', views.Cart.as_view(), name="cart"),
	path('checkout/', views.Checkout.as_view(), name="checkout"),
	path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),
]