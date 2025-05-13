from django.contrib import admin
from django.urls import path, include
from posts.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('users/', include('users.urls', namespace='users')),
    path('post', include('posts.urls', namespace='posts'))
]
