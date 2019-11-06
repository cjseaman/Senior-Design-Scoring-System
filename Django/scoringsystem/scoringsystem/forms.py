from django import forms
import logging

class TestScoreForm(forms.Form):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('Inside TestScoreForm')
    project_id = forms.CharField()
    judge_email = forms.CharField()
