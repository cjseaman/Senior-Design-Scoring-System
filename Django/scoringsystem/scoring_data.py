# scoring_data.py

from django.db import models

class Score(models.Model):
    project_id = models.PositiveIntegerField(default=0, primary_key=True)
    judge_email = models.CharField(max_length=128, default='', primary_key=True)
    dp_a = models.FloatField(default=0)
    dp_b = models.FloatField(default=0)
    dp_c = models.FloatField(default=0)
    dp_d = models.FloatField(default=0)
    dp_e = models.FloatField(default=0)
    dp_f = models.FloatField(default=0)
    dp_g = models.FloatField(default=0)
    dp_h = models.FloatField(default=0)
    p_a = models.FloatField(default=0)
    p_b = models.FloatField(default=0)
    p_c = models.FloatField(default=0)
    p_d = models.FloatField(default=0)
    econ_consideration = models.BooleanField(default=False)
    envi_consideration = models.BooleanField(default=False)
    sust_consideration = models.BooleanField(default=False)
    manu_consideration = models.BooleanField(default=False)
    ethi_consideration = models.BooleanField(default=False)
    heal_consideration = models.BooleanField(default=False)
    soci_consideration = models.BooleanField(default=False)
    poli_consideration = models.BooleanField(default=False)
    comments = models.TextField()
