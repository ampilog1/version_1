from django.urls import path
from . import views

app_name = 'learning_app'
urlpatterns = [
    # Домашняя страница.
    path('', views.home, name='home'),
]