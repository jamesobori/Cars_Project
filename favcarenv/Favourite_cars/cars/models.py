from django.db import models

# Create your models here.
class Cars(models.Model):
    tittle = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    speed = models.CharField(max_length=50)
    def __str__(self):
        return self.tittle

class Contact(models.Model):
    name = models.CharField(max_length= 100)
    email = models.CharField(max_length= 30)
    message = models.CharField(max_length= 1000)
    def __str__(self):
        return self.name
    
