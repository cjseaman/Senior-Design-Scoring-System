#views.py
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import logging
from scoringsystem import forms
from scoringsystem import models as m


# EXAMPLE:
#class HomePageView(TemplateView):
#    template_name = 'home.html'

def testScoreView(request):
    return render(request, 'test_score.html')

def submittedView(request):
    testSubmitScore(request)
    return render(request, 'submitted.html')

@csrf_exempt
def testSubmitScore(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('got to testSubmitScore!!')
    logging.debug(str(request))
    if request.method == 'POST':
        form = forms.TestScoreForm(request.POST)
        if form.is_valid():
            #logging.debug('inside post')
            project_id = request.POST.get("project_id")
            logging.debug('project_id: ', project_id)
            judge_email = request.POST.get("judge_email")
            logging.debug('judge_email: ', judge_email)
            #logging.debug('about to save as TestScore')
            score = m.TestScore(project_id=project_id, judge_email=judge_email)
            #logging.debug('got to testSubmitScore!!')
            score.save()
            return render(request, 'submitted.html')
    else:
        logging.debug('form was not POST')
        form = forms.TestScoreForm()

    return render(request,'submitted.html')
