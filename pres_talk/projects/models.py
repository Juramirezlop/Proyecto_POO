from django.db import models

# Create your models here.
#Models are the  classes that are referred to
#databases tables

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    

