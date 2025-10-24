from django.db import models

# Create your models here.
class USERS_DATA(models.Model):
    Full_Name=models.CharField()
    Email=models.EmailField(unique=True,max_length=254)
    Contact_Number=models.CharField(max_length=14)
    About_Project=models.CharField(max_length=1000)