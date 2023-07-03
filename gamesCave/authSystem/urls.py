from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('logout', views.logOutUser, name = 'logOutUser' ),
    path('login', views.logInUser, name = 'loginUser' ),
]
