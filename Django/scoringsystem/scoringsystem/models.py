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

class JudgeEval(m.Model):
    judge_email = m.CharField(max_length=128, primary_key=True)
    discipline = m.CharField(max_length=5)
    q1 = m.IntegerField(default=0)
    q2 = m.IntegerField(default=0)
    q3 = m.IntegerField(default=0)
    q4 = m.IntegerField(default=0)
    q5 = m.IntegerField(default=0)
    q6 = m.IntegerField(default=0)
    q7 = m.IntegerField(default=0)
    q8 = m.IntegerField(default=0)
    q9 = m.IntegerField(default=0)
    q10 = m.IntegerField(default=0)
    q11 = m.IntegerField(default=0)
    q12 = m.IntegerField(default=0)
    comments = m.CharField(max_length=512)

class review_session(m.Model):
    session_id = m.IntegerField(default=0, primary_key=True)
    name = m.CharField(max_length=128)
    location = m.CharField(max_length=128)

class judge(m.Model):
    email = m.CharField(max_length=128, primary_key=True)
    name = m.CharField(max_length=128)
    assigned_session_id = m.IntegerField(default=0)

class project(m.Model):
    project_id = m.IntegerField(default=0, primary_key=True)
    assigned_session_id = m.IntegerField(default=0)
    name = m.CharField(max_length=128)
    group_members = m.CharField(max_length=256)
    project_description = m.CharField(max_length=256)
    average_score = m.FloatField(default=0)

