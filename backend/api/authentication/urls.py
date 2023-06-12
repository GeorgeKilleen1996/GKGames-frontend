from django.urls import path
from .views import LoginView, RegistrationView

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/register/', RegistrationView.as_view(), name='register'),
]