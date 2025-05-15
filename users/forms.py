from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User
from django import forms

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control'
    }))
    
    pass

class SignForm(UserCreationForm):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control'
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control'
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control'
    }))
    
    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : 'form-control'
    }))
    
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class' : 'form-control'}), required=False)
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-control'
    }))
    
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : 'form-control'}), required=False)
    
    # date_birth = forms.DateField(widget=forms.DateInput(attrs={
    #     'class' : 'form-control'
    # }))
    
    position = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control'}), required=False)
    
    # fronend = forms.MultipleChoiceField(attrs={
    #     'class' : 'form-control'
    # })
    
    # backend = forms.MultipleChoiceField(attrs={
    #     'class' : 'form-control'
    # }), required=False
    
    # tools = forms.MultipleChoiceField(attrs={
    #     'class' : 'form-control'
    # })
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control'
    }))
    
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'age',
            'image',
            'email',
            'phone_number',
            'date_birth',
            'position',
            'fronend',
            'backend',
            'tools',
            'password1',
            'password2'
        )
        
class Edit_Profile(UserChangeForm):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control'
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control'
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control', 'readonly' : True
    }))
    
    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : 'form-control'
    }))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-control', 'readonly' : True
    }))
    
    position = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control'}), required=False)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'fronend', 'backend', 'tools', 'position', 'username', 'age')