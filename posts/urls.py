from django.urls import path
from .views import category, creation_post, save_post, save_post_view

app_name = 'posts'

urlpatterns = [
    path('category/<int:category_id>/', category, name='category'),
    path('create/post/', creation_post, name='creation_post'),
    path('save/post/<int:post_id>/', save_post, name="save_post"),
    path('yout/post/', save_post_view, name="save_post_view")
]
