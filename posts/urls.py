from django.urls import path
from .views import category

app_name = 'posts'

urlpatterns = [
    path('category/<int:category_id>/', category, name='category')
]
