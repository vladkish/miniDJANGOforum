from django.db import models
from users.models import User

class Category(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.title}'
    
    def count_post(self):
        return Post.objects.filter(category=self.title).count()
    
class Post(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to='posts_image/')
    date_public = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='posts')
    
    def __str__(self):
        return f'{self.title}, {self.description} author === {self.author}'
    
class SavePost(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='save_post')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='save_post')
    
    def __str__(self):
        return f'{self.post} for {self.user}'