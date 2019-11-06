#views.py
from django.views.generic import TemplateView
from django.shortcuts import render
from models import TestScore
from django.views.decorators.csrf import csrf_exempt

# EXAMPLE:
#class HomePageView(TemplateView):
#    template_name = 'home.html'

class TestScoreView(TemplateView):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('got to TestScoreView!!')
    template_name = 'test_score.html'

class SubmittedView(TemplateView):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('got to SubmittedView!!')
    template_name = 'submitted.html'
