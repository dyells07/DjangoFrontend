from django.db import models

# Create your models here.
class contact(models.Model):
    fname = models.CharField( max_length=120)
    lname = models.CharField( max_length=120)
    username=models.CharField( max_length=120)
    city=models.CharField( max_length=120)
    message=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.username
    