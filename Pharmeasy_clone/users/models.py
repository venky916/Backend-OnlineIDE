from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(User):
    GENDER=[
        ("M","Male"),
        ("F","Female"),
        ("O","Others")
    ]
    gender=models.CharField(max_length=1,choices=GENDER)
    date_of_birth=models.DateField()
    
    
class Prescription(models.Model):
    image_url=models.CharField(max_length=200)
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)
