from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Session(models.Model):
	sessionDate = models.DateTimeField(auto_now=False, auto_now_add=False)
	addJudge = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
