
from django import forms
from django.contrib.auth.models import User  
from .models import BlogPost,Comment,Business
class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'email','contact']