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
    session_list = m.session.objects.all()
    return render(request, 'admin_home.html', {'session_list': session_list})

def sdExperienceResults(request):
    eval_list = m.JudgeEval.objects.all()
    bio = len(m.JudgeEval.objects.filter(discipline='bioe'))
    civil = len(m.JudgeEval.objects.filter(discipline='civil'))
    coen = len(m.JudgeEval.objects.filter(discipline='coen'))
    elen = len(m.JudgeEval.objects.filter(discipline='elen'))
    mech = len(m.JudgeEval.objects.filter(discipline='mech'))
    inter = len(m.JudgeEval.objects.filter(discipline='inter'))
    return render(request, 'sd_experience.html', {
        'bio': bio,
        'civil': civil,
        'coen': coen,
        'elen': elen,
        'mech': mech,
        'inter': inter
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
    return render(request, 'add_projects_form.html', {
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
    return render(request, 'create_session_form.html')

def submitSessionView(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('inside submitSessionView')
    return submitSession(request)

def deleteSessionPromptView(request):
    session_id = request.POST.get('session_id')
    return render(request, 'delete_session_prompt.html', {'session_id': session_id})

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
    return render(request, 'deleted_session.html')



def assignJudgesView(request):
    session_id = request.POST.get('session_id')
    sessions = m.session.objects.filter(id=session_id)
    judge_list = m.judge.objects.filter(session_id=session_id)
    session_name = ''
    for s in sessions:
        session_name = s.session_name
    return render(request, 'add_judges_form.html', {
            'session_id': session_id,
            'session_name': session_name,
            'judge_list': judge_list
    })

def submittedAssignJudgesView(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('inside submittedAssignJudgesView')
    return submitAndAddJudge(request)

def judgeHomeView(request):
    return render(request, 'judge_home.html')

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
            session_id=session_id
        )
        logging.debug('judge:', judge)
        judge.save()
        return render(request, 'submitted_judge.html', {'session_id': session_id})
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
        project = m.project(
            session_id=session_id,
            project_name=project_name,
            group_members=group_members,
            project_desc=project_desc,
            average_score=average_score
        )
        logging.debug('project:', project)
        project.save()
        return render(request, 'submitted.html')
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
