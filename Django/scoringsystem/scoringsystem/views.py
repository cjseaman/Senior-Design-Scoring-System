#views.py
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from scoringsystem import forms
from scoringsystem import models as m
import logging

def projectEvalView(request):
    return render(request, 'projects_eval_form.html')

def judgeExpEvalView(request):
    return render(request, 'judge_exp_eval_form.html')

def submitJudgeExpEvalView(request):
    return submitJudgeEval(request)

def submitProjectEvalView(request):
    return submitProjectEval(request)

def adminHomeView(request):
    return render(request, 'admin_home.html')

def submittedCreatedSessionView(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('inside submittedCreatedSessionView')
    return submitCreatedSession(request)

def createSessionView(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('inside createSessionView')
    return render(request, 'create_session_form.html')

def submitSessionView(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('inside submitSessionView')
    return submitSession(request)

def assignJudgesView(request):
    return render(request, 'add_judges_form.html')

def judgeHomeView(request):
    return render(request, 'judge_home.html')

def submitCreatedSession(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('got to submitCreatedSession!!')
    if request.method == 'POST':
        logging.debug('form is valid')
        session_name = request.POST.get('name')
        session_location = request.POST.get('location')
        session = m.session(
            session_name=session_name,
            session_location=session_location
        )
        logging.debug('session:', session)
        session.save()
        return render(request, 'submitted.html')
    else:
        logging.debug('method is not POST')

    return render(request,'error.html')

"""@csrf_exempt
def submitSession(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('got to submitSession!!')
    if request.method == 'POST':
        logging.debug('form is valid')
        session_id = request.POST.get('session_id')
        name = request.POST.get('name')
        location = request.POST.get('location')
        session = m.review_session(
            session_id = session_id,
            name = name,
            location = location
        )
        logging.debug('session:', session)
        session.save()
        return render(request, 'submitted.html')

    else:
        logging.debug('method is not POST')

    return render(request,'error.html')"""

@csrf_exempt
def submitJudgeEval(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('got to submitJudgeEval!!')
    if request.method == 'POST':
        logging.debug('form is valid')
        judge_email = request.POST.get("judge_email")
        discipline = request.POST.get("discipline")
        q1 = int(request.POST.get("q1"))
        q2 = int(request.POST.get("q2"))
        q3 = int(request.POST.get("q3"))
        q4 = int(request.POST.get("q4"))
        q5 = int(request.POST.get("q5"))
        q6 = int(request.POST.get("q6"))
        q7 = int(request.POST.get("q7"))
        q8 = int(request.POST.get("q8"))
        q9 = int(request.POST.get("q9"))
        q10 = int(request.POST.get("q10"))
        q11 = int(request.POST.get("q11"))
        q12 = int(request.POST.get("q12"))
        comments = request.POST.get("comments")
        eval = m.JudgeEval(
            judge_email=judge_email, discipline=discipline, q1=q1, q2=q2, q3=q3,
            q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, q9=q9, q10=q10, q11=q11, q12=q12,
            comments=comments
        )
        logging.debug('eval:', eval)
        eval.save()
        return render(request, 'submitted.html')
    else:
        logging.debug('method is not POST')

    return render(request,'error.html')


def makeBool(val):
    if val == 'true':
        return True
    return False

@csrf_exempt
def submitProjectEval(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('got to submitProjectEval!!')
    if request.method == 'POST':
        logging.debug('form is valid')
        project_id = request.POST.get("project_id")
        judge_email = request.POST.get("judge_email")
        dp_a = request.POST.get("dp_a")
        dp_b = request.POST.get("dp_b")
        dp_c = request.POST.get("dp_c")
        dp_d = request.POST.get("dp_d")
        dp_e = request.POST.get("dp_e")
        dp_f = request.POST.get("dp_f")
        dp_g = request.POST.get("dp_g")
        dp_h = request.POST.get("dp_h")
        p_a = request.POST.get("p_a")
        p_b = request.POST.get("p_b")
        p_c = request.POST.get("p_c")
        p_d = request.POST.get("p_d")
        econ_consideration = makeBool(request.POST.get("econ_consideration"))
        envi_consideration = makeBool(request.POST.get("envi_consideration"))
        sust_consideration = makeBool(request.POST.get("sust_consideration"))
        manu_consideration = makeBool(request.POST.get("manu_consideration"))
        ethi_consideration = makeBool(request.POST.get("ethi_consideration"))
        heal_consideration = makeBool(request.POST.get("heal_consideration"))
        soci_consideration = makeBool(request.POST.get("soci_consideration"))
        poli_consideration = makeBool(request.POST.get("poli_consideration"))
        comments = request.POST.get("comments")
        score = m.ProjectEval(
            project_id=project_id, judge_email=judge_email, dp_a=dp_a,
            dp_b=dp_b, dp_c=dp_c, dp_d=dp_d, dp_e=dp_e, dp_f=dp_f,
            dp_g=dp_g, dp_h=dp_h, p_a=p_a, p_b=p_b, p_c=p_c, p_d=p_d,
            econ_consideration=econ_consideration,
            envi_consideration=envi_consideration,
            sust_consideration=sust_consideration,
            manu_consideration=manu_consideration,
            ethi_consideration=ethi_consideration,
            heal_consideration=heal_consideration,
            soci_consideration=soci_consideration,
            poli_consideration=poli_consideration,
            comments=comments
        )
        logging.debug('score:', score)
        score.save()
        return render(request, 'submitted.html')
    else:
        logging.debug('method is not POST')

    return render(request,'error.html')
