from django.db import models

# Create your models here.
class Judge(models.Model):
	firstName = models.CharField(max_length=120)
	lastName = models.CharField(max_length=120)