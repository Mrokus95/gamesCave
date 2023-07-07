from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('logout/', views.logOutUser, name = 'logOutUser' ),
    path('login/', views.logInUser, name = 'loginUser' ),
    path('password_change/', views.CustomPaswordChangeView.as_view(), name = 'passwordChange'),
    path('password_change/done/', views.CustomPaswordChangeDoneView.as_view(), name = 'passwordChangeDone'),
    path('oauth/', include('social_django.urls', namespace='social')),
]
