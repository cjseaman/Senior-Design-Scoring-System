# File: models.py
# Description: Class definitions for Django models.

from django.db import models as m
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager

# Class: ProjectEval
# Description: Class definition for project evaluation form.
class ProjectEval(m.Model):
    id = m.AutoField(primary_key=True)
    project_id = m.IntegerField(default=0)
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

    class Meta:
        unique_together = (("project_id", "judge_email"),)

# Class: JudgeEval
# Description: Class definition for judge experience evaluation form.
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

# Class: session
# Description: Class definition for session.
class session(m.Model):
    session_name = m.CharField(max_length=128)
    session_location = m.CharField(max_length=128)
    id = m.AutoField(primary_key=True)
    class Meta:
        db_table = 'scoringsystem_session'

# Class: judge
# Description: Class definition for judge, including login information.
class judge(AbstractBaseUser):
    judge_name = m.CharField(max_length=128)
    judge_email = m.CharField(max_length=128, primary_key=True)
    session_id = m.IntegerField(default=0)
    is_admin = m.BooleanField(default=False)
    USERNAME_FIELD = 'judge_email'
    EMAIL_FIELD = 'judge_email'
    REQUIRED_FIELDS = ['judge_name']
    objects = UserManager()

# Class: project
# Description: Class definition for project.
class project(m.Model):
    session_id = m.IntegerField(default=0)
    project_name = m.CharField(max_length=128)
    group_members = m.CharField(max_length=256)
    project_desc = m.CharField(max_length=256)
    average_score = m.FloatField(default=0)
    id = m.AutoField(primary_key=True)

# Class: judgeUser
# Description: Class definition for judge as a user.
class judgeUser(m.Model):
    user_email = m.CharField(max_length=128, primary_key=True)
    password = m.CharField(max_length=128)
