from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
