from django.db import models
from listing.models import Property
# Create your models here.
class Inquiry(models.Model):
    
     GENDER_CHOICES=[
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    ]
    
    
    
     property = models.ForeignKey(Property, on_delete=models.CASCADE)
     name = models.CharField(max_length=100)
     gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
     phone=models.CharField(max_length=13)
     email = models.EmailField(max_length=254)
     message = models.TextField(max_length=500,blank=True)
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.name
    