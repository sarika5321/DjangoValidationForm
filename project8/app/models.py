from django.db import models

# Create your models here.

class school(models.Model):
    sname = models.CharField(max_length=50,primary_key=True)
    sprincipal = models.CharField(max_length=50)
    saddress = models.CharField(max_length=50)
    
    def __str__(self):
        return self.sname
    