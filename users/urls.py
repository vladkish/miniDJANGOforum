from django.urls import path
from .views import main, login, sign, logout, profile, edit_profile

app_name = 'users'

urlpatterns = [
    path('main/', main, name='main'),
    path('login/', login, name='login'),
    path('sign/', sign, name='sign'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile')
]
