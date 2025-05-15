from django.contrib import admin
from django.urls import path, include
from posts.views import index

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('users/', include('users.urls', namespace='users')),
    path('post', include('posts.urls', namespace='posts')),
]

# Добавление обработки медиа фалов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)