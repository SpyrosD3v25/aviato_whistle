"""
This file is responsible for making the models for home app. 
"""

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

CATEGORY_CHOICES = (
    ("1", "I do not know now"),
    ("2", "Natural Disaster"),
    ("3", "Natural Disaster - fires"),
    ("4", "Natural Disaster - earthquake"),
    ("5", "Natural Disaster - Destruction of Public Property"),
    ("6", "Natural Disaster - Pollution"),
    ("7", "Crime - Pollution"),
    ("8", "Crime - Destruction of Public Property"),
    ("9", "Crime - Beating"),
    ("10", "Crime - Theft"),
    ("11", "Crime"),
)

DHMOS_CHOISES = (
    ("1", "Example of Municipality1"),
    ("2", "Example Municipality2"),
    ("3", "Example of Municipality3"),
    ("4", "Example of Municipality4"),
    ("5", "Example of Municipality5"),
    ("6", "Example of Municipality6"),
    ("7", "Example of Municipality7"),
    ("8", "Example of Municipality8"),
    ("9", "Example of Municipality9"),
    ("10", "Example of Municipality 10"),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

class BlogPost(models.Model):
    title=models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    #slug=models.CharField(max_length=130)
    content=models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Δεν γνωρίζω')
    dhmos = models.CharField(max_length=50, choices=DHMOS_CHOISES, default='Παράδειγμα Δήμου1')
    image = models.ImageField(upload_to="media", blank=True, null=True)
    location = models.CharField(max_length=255, default="None")
    dateTime=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title
    
    def get_absolute_url(self):
        return reverse('blogs')
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username +  " Comment: " + self.content
    

