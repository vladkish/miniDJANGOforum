from django.urls import path
from .views import main, login, sign, logout

app_name = 'users'

urlpatterns = [
    path('main/', main, name='main'),
    path('login/', login, name='login'),
    path('sign/', sign, name='sign'),
    path('logout/', logout, name='logout')
]
