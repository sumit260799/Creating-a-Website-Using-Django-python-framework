import email
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=20)
    phone=models.CharField(max_length=10)
    date=models.DateField()
    
    
    def __str__(self):
        return self.name
     
   
      
    