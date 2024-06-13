from django.urls import path, include
from .api import views

urlpatterns = [
    path('register/', views.APIRegisterView.as_view(), name='register'),
    path('login/', views.LoginApiView.as_view(), name='login'),
]
