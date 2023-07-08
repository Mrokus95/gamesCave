from django.urls import path, include
from . import views

urlpatterns = [
    # Basic endpoints
    path('register/', views.register, name = 'register'),
    path('logout/', views.logOutUser, name = 'logOutUser' ),
    path('login/', views.logInUser, name = 'loginUser' ),

    #Changing password
    path('password_change/', views.CustomPaswordChangeView.as_view(), name = 'passwordChange'),
    path('password_change/done/', views.CustomPaswordChangeDoneView.as_view(), name = 'passwordChangeDone'),

    #Reset password
    path('reset_password/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),    
    path('reset_password/complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
   
    #Social Login
    path('oauth/', include('social_django.urls', namespace='social')),
]
