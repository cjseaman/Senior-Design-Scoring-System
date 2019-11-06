from django import forms
import logging

class TestScoreForm(forms.Form):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('Inside TestScoreForm')
    project_id = models.CharField(max_length=128, default='')
    judge_email = models.CharField(max_length=128, default='')
