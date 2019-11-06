from django.db import models
import logging

class TestScore(models.Model):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('Inside TestScore model')
    project_id = models.CharField(max_length=128, default='', primary_key=True)
    judge_email = models.CharField(max_length=128, default='')
