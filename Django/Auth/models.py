from django.db import models

class Auth(models.Model):
    user_name = models.EmailField(blank=False)
    password = models.CharField(max_length= 128, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
