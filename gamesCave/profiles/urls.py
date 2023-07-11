from django.urls import path
from . import views

urlpatterns = [
    path('edit', views.editUserDataView, name='editUserData'),
]
