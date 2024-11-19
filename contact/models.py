from django.db import models
from django.urls import reverse
from datetime import datetime, date
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    user_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    name = models.CharField(max_length=225)
    profile_image = models.ImageField(upload_to='contact_images/', blank=True, null=True)  # Optional profile image
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    contact_number = models.CharField( max_length=15,  validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',  # Allows for optional "+" at the start
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ])
    email = models.EmailField(max_length=255)
    post_date = models.DateTimeField(auto_now_add = True)

    
    def __str__ (self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse('contact-list')


