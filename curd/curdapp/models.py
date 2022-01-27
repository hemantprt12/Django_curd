from django.db import models

# Create your models here.
class UserDetails(models.Model):
    User_Id = models.IntegerField()
    User_Name = models.CharField(max_length=40)
    User_Address = models.CharField(max_length=50)
