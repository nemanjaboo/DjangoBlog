from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('userpage/', views.userpage, name='userpage'),
    path('profile/<str:username>/', views.profile, name='profile'),
]
