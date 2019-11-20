#views.py
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from scoringsystem import forms
from scoringsystem import models as m
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user, login
from django.contrib.auth import logout
from django.core.mail import send_mail
from smtplib import SMTPRecipientsRefused
import logging
import string
import random

def logoutView(request):
    logout(request)
    return render(request, 'logout.html')

def loginView(request):
    return render(request, 'registration/login.html')

def loginUserView(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request=request, username=email, password=password)
    if user is not None:
        login(request, user)
        if user.is_admin == True:
            return render(request, 'admin/submitted.html')
        else:
            return judgeHomeView(request)
        return loginView(request)
    else:
        return loginView(request)

def projectEvalView(request):
    project_id = request.POST.get('project_id')
    judge = get_user(request)
    return render(request, 'judge/projects_eval_form.html', {'project_id':project_id, 'judge': judge})

def judgeExpEvalView(request):
    judge = get_user(request)
    return render(request, 'judge/judge_exp_eval_form.html', {'judge': judge})

def submitJudgeExpEvalView(request):
    return submitJudgeEval(request)

def submitProjectEvalView(request):
    return submitProjectEval(request)

def adminHomeView(request):
    session_list = m.session.objects.all()
    return render(request, 'admin/admin_home.html', {'session_list': session_list})

def sdExperience(request):
    eval_list = m.JudgeEval.objects.all()
    q1_average = 0
    q2_average = 0
    q3_average = 0
    q4_average = 0
    q5_average = 0
    q6_average = 0
    q7_average = 0
    q8_average = 0
    q9_average = 0
    q10_average = 0
    q11_average = 0
    q12_average = 0
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    n6 = 0
    n7 = 0
    n8 = 0
    n9 = 0
    n10 = 0
    n11 = 0
    n12 = 0
    for eval in eval_list:
        if(eval.q1 != 0):
            n1 = n1 + 1
            q1_average += eval.q1
        if(eval.q2 != 0):
            n2 = n2 + 1
            q2_average += eval.q2
        if(eval.q3 != 0):
            n3 = n3 + 1
            q3_average += eval.q3
        if(eval.q4 != 0):
            n4 = n4 + 1
            q4_average += eval.q4
        if(eval.q5 != 0):
            n5 = n5 + 1
            q5_average += eval.q5
        if(eval.q6 != 0):
            n6 = n6 + 1
            q6_average += eval.q6
        if(eval.q7 != 0):
            n7 = n7 + 1
            q7_average += eval.q7
        if(eval.q8 != 0):
            n8 = n8 + 1
            q8_average += eval.q8
        if(eval.q9 != 0):
            n9 = n9 + 1
            q9_average += eval.q9
        if(eval.q10 != 0):
            n10 = n10 + 1
            q10_average += eval.q10
        if(eval.q11 != 0):
            n11 = n11 + 1
            q11_average += eval.q11
        if(eval.q12 != 0):
            n12 = n12 + 1
            q12_average += eval.q12
    if n1 is not 0:
        q1_average /= n1
    if n2 is not 0:
        q2_average /= n2
    if n3 is not 0:
        q3_average /= n3
    if n4 is not 0:
        q4_average /= n4
    if n5 is not 0:
        q5_average /= n5
    if n6 is not 0:
        q6_average /= n6
    if n7 is not 0:
        q7_average /= n7
    if n8 is not 0:
        q8_average /= n8
    if n9 is not 0:
        q9_average /= n9
    if n10 is not 0:
        q10_average /= n10
    if n11 is not 0:
        q11_average /= n11
    if n12 is not 0:
        q12_average /= n12

    return render(request, 'admin/sd_experience.html', {
        'q1_average': q1_average,
        'q2_average': q2_average,
        'q3_average': q3_average,
        'q4_average': q4_average,
        'q5_average': q5_average,
        'q6_average': q6_average,
        'q7_average': q7_average,
        'q8_average': q8_average,
        'q9_average': q9_average,
        'q10_average': q10_average,
        'q11_average': q11_average,
        'q12_average': q12_average,
    })

def sdExperienceResults(request):
    eval_list = m.JudgeEval.objects.all()
    return render(request, 'admin/sd_experience_results.html', {
        'sd_exp_list': eval_list
    })

def submittedCreatedSessionView(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('inside submittedCreatedSessionView')
    return submitCreatedSession(request)

def createProjectForm(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('inside createProjectForm')
    session_id = request.POST.get('session_id')
    sessions = m.session.objects.filter(id=session_id)
    project_list = m.project.objects.filter(session_id=session_id)
    session_name = ''
    for s in sessions:
        session_name = s.session_name
    return render(request, 'admin/add_projects_form.html', {
        'session_id': session_id,
        'session_name': session_name,
        'project_list': project_list
    })

def submittedCreatedProjectForm(request):
    session_id = request.POST.get('session_id')
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('inside submittedCreatedProjectForm')
    return submitCreatedProject(request)

def createSessionView(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('inside createSessionView')
    return render(request, 'admin/create_session_form.html')

def submitSessionView(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('inside submitSessionView')
    return submitSession(request)

def deleteSessionPromptView(request):
    session_id = request.POST.get('session_id')
    return render(request, 'admin/delete_session_prompt.html', {'session_id': session_id})

def deleteSessionView(request):
    session_id = request.POST.get('session_id')

    judges = m.judge.objects.filter(session_id=session_id)
    for judge in judges:
        m.JudgeEval.objects.filter(judge_email=judge.judge_email).delete()
    judges.delete()

    projects = m.project.objects.filter(session_id=session_id)
    for project in projects:
        m.ProjectEval.objects.filter(project_id=project.id).delete()
    projects.delete()

    m.session.objects.filter(id=session_id).delete()
    return render(request, 'admin/deleted_session.html')



def assignJudgesView(request):
    session_id = request.POST.get('session_id')
    sessions = m.session.objects.filter(id=session_id)
    judge_list = m.judge.objects.filter(session_id=session_id)
    session_name = ''
    for s in sessions:
        session_name = s.session_name
    return render(request, 'admin/add_judges_form.html', {
            'session_id': session_id,
            'session_name': session_name,
            'judge_list': judge_list
    })

def submittedAssignJudgesView(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('inside submittedAssignJudgesView')
    return submitAndAddJudge(request)

def judgeHomeView(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    judge = get_user(request)
    session_id = judge.session_id
    session = m.session.objects.get(id=session_id)
    project_list = m.project.objects.filter(session_id=session_id)
    return render(request, 'judge/judge_home.html', {
        'judge': judge,
        'session': session,
        'session_id': session_id,
        'project_list': project_list
    })

def submitAndAddJudge(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('got to submitAndAddJudge!!')
    if request.method == 'POST':
        logging.debug('form is valid')
        judge_email = request.POST.get('judge_email')
        judge_name = request.POST.get('judge_name')
        session_id = request.POST.get('session_id')
        judge = m.judge(
            judge_email=judge_email,
            judge_name=judge_name,
            session_id=session_id,
        )
        #To be used later
        password = randomPassword()
        #password = 'testpassword'
        judge.set_password(password)
        message = (
            'Hi ' + judge_name + ',\n'
            'Your password is: "' + password + '".\n'
            'Use your email and this password to log in to the senior design scoring system.'
        )

        try:
            send_mail('Senior Design Scoring System Password', message, 'scusdscoringsystem@gmail.com', [judge_email], fail_silently=False)
        except SMTPRecipientsRefused:
            return render(request, 'admin/email_error.html', {'email': judge_email})

        logging.debug('judge:', judge)
        judge.save()
        return render(request, 'admin/submitted_judge.html', {'session_id': session_id})
    else:
        logging.debug('method is not POST')

    return render(request,'error.html')

def submitCreatedProject(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('got to submitCreatedProject!!')
    if request.method == 'POST':
        logging.debug('form is valid')
        session_id = request.POST.get('session_id')
        project_name = request.POST.get('project_name')
        group_members = request.POST.get('group_members')
        project_desc = request.POST.get('project_desc')
        average_score = request.POST.get('average_score')
        if average_score is None:
            average_score = 0
        project = m.project(
            session_id=session_id,
            project_name=project_name,
            group_members=group_members,
            project_desc=project_desc,
            average_score=average_score
        )
        logging.debug('project:', project)
        project.save()
        return render(request, 'admin/submitted.html')
    else:
        logging.debug('method is not POST')

    return render(request,'error.html')

def submitCreatedSession(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('got to submitCreatedSession!!')
    if request.method == 'POST':
        logging.debug('form is valid')
        session_name = request.POST.get('name')
        session_location = request.POST.get('location')
        session = m.session(
            session_name=session_name,
            session_location=session_location,
        )
        logging.debug('session:', session)
        session.save()
        return render(request, 'admin/submitted.html')
    else:
        logging.debug('method is not POST')

    return render(request,'error.html')

@csrf_exempt
def submitJudgeEval(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('got to submitJudgeEval!!')
    judge = get_user(request)
    judge_email = judge.judge_email
    if request.method == 'POST':
        logging.debug('form is valid')
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
        return render(request, 'judge/submitted.html')
    else:
        logging.debug('method is not POST')

    return render(request,'error.html')


def makeBool(val):
    if val == 'true':
        return True
    return False

@csrf_exempt
def submitProjectEval(request):
    judge_email = request.POST.get('judge_email')
    judge = m.judge.objects.filter(email=judge_email)
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
        return judgeHomeView(request)
    else:
        logging.debug('method is not POST')

    return render(request,'error.html')

def randomPassword(stringLength=10):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
