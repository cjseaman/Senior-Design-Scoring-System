# m.py

from django.db import models as m

class ProjectEval(m.Model):
    project_id = m.IntegerField(default=0, primary_key=True)
    judge_email = m.CharField(max_length=128, default='')
    dp_a = m.IntegerField(default=0)
    dp_b = m.IntegerField(default=0)
    dp_c = m.IntegerField(default=0)
    dp_d = m.IntegerField(default=0)
    dp_e = m.IntegerField(default=0)
    dp_f = m.IntegerField(default=0)
    dp_g = m.IntegerField(default=0)
    dp_h = m.IntegerField(default=0)
    p_a = m.IntegerField(default=0)
    p_b = m.IntegerField(default=0)
    p_c = m.IntegerField(default=0)
    p_d = m.IntegerField(default=0)
    econ_consideration = m.BooleanField(default=False)
    envi_consideration = m.BooleanField(default=False)
    sust_consideration = m.BooleanField(default=False)
    manu_consideration = m.BooleanField(default=False)
    ethi_consideration = m.BooleanField(default=False)
    heal_consideration = m.BooleanField(default=False)
    soci_consideration = m.BooleanField(default=False)
    poli_consideration = m.BooleanField(default=False)
    comments = m.CharField(max_length=512)
