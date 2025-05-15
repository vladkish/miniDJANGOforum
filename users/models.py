from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

class User(AbstractUser):
    
    frontend_list = (
        ('js', 'Js'),
        ('css', 'CSS'),
        ('html', 'html'),
        ('figma', 'figma')
    )
    
    backend_list = (
        ('php', 'PHP'),
        ('python', 'Python'),
        ('csharp', 'C#'),
        ('django', 'Django'),
        ('laver', 'Laver'),
        ('Go', 'Go')
    )
    
    tools_list = (
        ('docker', 'Docker'),
        ('git', 'Git'),
        ('webpack', 'Webpack'),
    )
    
    image = models.ImageField(upload_to='users_image/')
    description = models.TextField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(default=18)
    phone_number = PhoneNumberField(region="UA", blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=180)
    
    fronend = MultiSelectField(choices=frontend_list, blank=True, null=True)
    backend = MultiSelectField(choices=backend_list, blank=True, null=True)
    tools = MultiSelectField(choices=tools_list, blank=True, null=True)