from django import forms

class ProjectEvalForm(forms.Form):
    project_id = forms.IntegerField()
    judge_email = forms.CharField(max_length=128)
    dp_a = forms.IntegerField()
    dp_b = forms.IntegerField()
    dp_c = forms.IntegerField()
    dp_d = forms.IntegerField()
    dp_e = forms.IntegerField()
    dp_f = forms.IntegerField()
    dp_g = forms.IntegerField()
    dp_h = forms.IntegerField()
    p_a = forms.IntegerField()
    p_b = forms.IntegerField()
    p_c = forms.IntegerField()
    p_d = forms.IntegerField()
    econ_consideration = forms.BooleanField()
    envi_consideration = forms.BooleanField()
    sust_consideration = forms.BooleanField()
    manu_consideration = forms.BooleanField()
    ethi_consideration = forms.BooleanField()
    heal_consideration = forms.BooleanField()
    soci_consideration = forms.BooleanField()
    poli_consideration = forms.BooleanField()
    comments = forms.CharField(max_length=512)

class JudgeEvalForm(forms.Form):
    judge_email = forms.CharField(max_length=128)
    discipline = forms.CharField(max_length=5)
    q1 = forms.CharField(max_length=1)
    q2 = forms.CharField(max_length=1)
    q3 = forms.CharField(max_length=1)
    q4 = forms.CharField(max_length=1)
    q5 = forms.CharField(max_length=1)
    q6 = forms.CharField(max_length=1)
    q7 = forms.CharField(max_length=1)
    q8 = forms.CharField(max_length=1)
    q9 = forms.CharField(max_length=1)
    q10 = forms.CharField(max_length=1)
    q11 = forms.CharField(max_length=1)
    q12 = forms.CharField(max_length=1)
    comments = forms.CharField(max_length=512)

class CreateSessionForm(forms.Form):
    session_name = forms.CharField(max_length=128)
    session_location = forms.CharField(max_length=128)

class CreateProjectForm(forms.Form):
    assigned_session_id = forms.IntegerField()
    name = forms.CharField(max_length=128)
    group_members = forms.CharField(max_length=256)
    project_description = forms.CharField(max_length=256)
    average_score = forms.FloatField()

class AddJudgeForm(forms.Form):
    email = forms.CharField(max_length=128)
    name = forms.CharField(max_length=128)
    assigned_session_id = forms.IntegerField()
