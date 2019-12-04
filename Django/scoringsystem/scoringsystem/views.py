# File: views.py
# Description: This file holds all the methods to display all the views and
#   render all the pages.

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
from django.core.exceptions import ObjectDoesNotExist
import logging
import string
import random

# Function name: logoutView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Logs out user from application.
def logoutView(request):
    logout(request)
    return render(request, 'logout.html')

# Function name: loginView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Logs in user to application.
def loginView(request):
    return render(request, 'registration/login.html')

# Function name: loginUserView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Logs in the user by submitting the login information.
def loginUserView(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request=request, username=email, password=password)
    if user is not None:
        login(request, user)
        if user.is_admin == True:
            return render(request, 'admin/submitted.html')
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: homeView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Renders the general home view.
def homeView(request):
    return render(request, 'home.html')

"""Judge Views"""

# Function name: judgeHomeView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the user is authenticated before rendering
#   the judge home view.
def judgeHomeView(request):
    judge = get_user(request)
    if(judge.is_authenticated):
        logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
        session_id = judge.session_id
        session = m.session.objects.get(id=session_id)
        project_list = m.project.objects.filter(session_id=session_id)
        return render(request, 'judge/judge_home.html', {
            'judge': judge,
            'session': session,
            'session_id': session_id,
            'project_list': project_list
        })
    else:
        return render(request, 'logout.html')

# Function name: projectEvalView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the user is authenticated before rendering
#   the projects evaluation form.
def projectEvalView(request):
    judge = get_user(request)
    if (judge.is_authenticated):
        project_id = request.POST.get('project_id')
        return render(request, 'judge/projects_eval_form.html', {'project_id':project_id, 'judge': judge})
    else:
        return render(request, 'logout.html')

# Function name: judgeExpEvalView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the user is authenticated before rendering
#   the experience evaluation form.
def judgeExpEvalView(request):
    judge = get_user(request)
    if(judge.is_authenticated):
        return render(request, 'judge/judge_exp_eval_form.html', {'judge': judge})
    else:
        return render(request, 'logout.html')

# Function name: submitJudgeExpEvalView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the user is authenticated before submitting
#   the judge evaluation form.
def submitJudgeExpEvalView(request):
    judge = get_user(request)
    if(judge.is_authenticated):
        return submitJudgeEval(request)
    else:
        return render(request, 'logout.html')

# Function name: submitProjectEvalView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the user is authenticated before rendering
#   the project evaluation form.
def submitProjectEvalView(request):
    judge = get_user(request)
    if(judge.is_authenticated):
        project_id = request.POST.get('project_id')
        return render(request, 'judge/projects_eval_form.html', {'project_id':project_id, 'judge': judge})
    else:
        return render(request, 'logout.html')

# Function name: sdExperience
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the user is authenticated before calculating and
#   rendering the averages of the senior design experience form.
def sdExperience(request):
    user = get_user(request)
    if(user.is_authenticated):
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
            q1_average = round(q1_average/n1, 2)
        if n2 is not 0:
            q2_average = round(q2_average/n2, 2)
        if n3 is not 0:
            q3_average = round(q3_average/n3, 2)
        if n4 is not 0:
            q4_average = round(q4_average/n4, 2)
        if n5 is not 0:
            q5_average = round(q5_average/n5, 2)
        if n6 is not 0:
            q6_average = round(q6_average/n6, 2)
        if n7 is not 0:
            q7_average = round(q7_average/n7, 2)
        if n8 is not 0:
            q8_average = round(q8_average/n8, 2)
        if n9 is not 0:
            q9_average = round(q9_average/n9, 2)
        if n10 is not 0:
            q10_average = round(q10_average/n10, 2)
        if n11 is not 0:
            q11_average = round(q11_average/n11, 2)
        if n12 is not 0:
            q12_average = round(q12_average/n12, 2)

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
    else:
        return render(request, 'logout.html')

# Function name: submitJudgeEval
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the user is authenticated before handling the
#   HTTP request and save the judge experience evaluation form in the database.
@csrf_exempt
def submitJudgeEval(request):
    judge = get_user(request)
    if(judge.is_authenticated):
        logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
        logging.debug('got to submitJudgeEval!!')
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
    else:
        return render(request, 'logout.html')

# Function name: submitProjectEval
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the user is authenticated before handling the
#   HTTP request and saves the project evaluation form in the database.
@csrf_exempt
def submitProjectEval(request):
    judge = get_user(request)
    if(judge.is_authenticated):
        logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
        logging.debug('got to submitProjectEval!!')
        if request.method == 'POST':
            logging.debug('form is valid')
            project_id = request.POST.get("project_id")
            judge_email = judge.judge_email
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
            m.ProjectEval.objects.filter(judge_email=judge.judge_email, project_id=project_id).delete()
            score.save()
            p = m.project.objects.get(id=project_id)
            p.average_score = averageScores(project_id)
            p.save()
            return render(request, 'judge/submitted.html')
        else:
            logging.debug('method is not POST')

        return render(request,'error.html')
    else:
        return render(request, 'logout.html')

# Admin Views

# Function name: adminHomeView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the admin is authenticated before rendering
#   the home page.
def adminHomeView(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
            session_list = m.session.objects.all()
            return render(request, 'admin/admin_home.html', {'session_list': session_list})
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: sdExperienceResults
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the admin is authenticated before rendering all
#   the senior design experience results.
def sdExperienceResults(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
            eval_list = m.JudgeEval.objects.all()
            return render(request, 'admin/sd_experience_results.html', {
                'sd_exp_list': eval_list
            })
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: submittedCreatedSessionView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the admin is authenticated before submitting
#   the created session.
def submittedCreatedSessionView(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
            logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
            logging.debug('inside submittedCreatedSessionView')
            return submitCreatedSession(request)
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: createProjectForm
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the admin is authenticated before creating
#   a project for a given session.
def createProjectForm(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
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
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: submittedCreatedProjectForm
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the admin is authenticated before submitting a created project.
def submittedCreatedProjectForm(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
            session_id = request.POST.get('session_id')
            logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
            logging.debug('inside submittedCreatedProjectForm')
            return submitCreatedProject(request)
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: createSessionView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the admin is authenticated before rendering a created session.
def createSessionView(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
            logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
            logging.debug('inside createSessionView')
            return render(request, 'admin/create_session_form.html')
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: submitSessionView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the admin is authenticated before submitting a session.
def submitSessionView(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
            logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
            logging.debug('inside submitSessionView')
            return submitSession(request)
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: deleteSessionPromptView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the admin is authenticated before prompting
#   a confirmation to delete the session.
def deleteSessionPromptView(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
            session_id = request.POST.get('session_id')
            return render(request, 'admin/delete_session_prompt.html', {'session_id': session_id})
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: deleteSessionView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the admin is authenticated before deleting a sesison.
def deleteSessionView(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
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
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: assignJudgesView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the admin is authenticated before rendering
#   the list of judges to a session.
def assignJudgesView(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
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
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: submittedAssignJudgesView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that the admin is authenticated before creating a judge.
def submittedAssignJudgesView(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
            logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
            logging.debug('inside submittedAssignJudgesView')
            return submitAndAddJudge(request)
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: submitAndAddJudge
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Submits and creates a new judge, sending them an email with
#   their login password.
def submitAndAddJudge(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
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
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: submitCreatedProject
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Submits and creates a new project.
def submitCreatedProject(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
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
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: submitCreatedSession
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Submits and creates a new session.
def submitCreatedSession(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
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
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: scoresSummaryView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that user is authenticaed before submitting
#   or displaying summary scores.
def scoresSummaryView(request):
    judge = get_user(request)
    if(judge.is_authenticated):
        if(judge.is_admin):
            session_id = request.POST.get('session_id')
            project_list = m.project.objects.filter(session_id=session_id)
            return render(request, 'admin/scores_summary.html', {'project_list': project_list, 'judge': judge})
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Function name: scoresDetailView
# Parameters:
#   request (Django HTTP request) - holds the HTTP request and associated data
# Returns: HttpResponse object with rendered template
# Description: Verifies that user is authenticaed before submitting
#   or displaying detailed scores.
def scoresDetailView(request):
    user = get_user(request)
    if(user.is_authenticated):
        if(user.is_admin):
            project_id = request.POST.get('project_id')
            scores_list = m.ProjectEval.objects.filter(project_id=project_id)
            project = m.project.objects.get(id=project_id)
            return render(request, 'admin/scores_detail.html', {'scores_list': scores_list, 'project': project})
        else:
            return render(request, 'judge/submitted.html')
    else:
        return render(request, 'logout.html')

# Utility functions

# Function name: randomPassword
# Parameters:
#   stringLength - (int) default value is 10
# Returns: string
# Description: Generate a random string of letters and digits
def randomPassword(stringLength=10):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

# Function name: averageScores
# Parameters:
#   project_id - (int) holds project ID
# Returns: rounded average score for project
# Description: Tallies up the total average score of a project
def averageScores(project_id):
    p = m.project.objects.get(id=project_id)
    judge_list = m.judge.objects.filter(session_id=p.session_id)
    all_scores_list = []
    average_score = 0
    for judge in judge_list:
        try:
            p = m.ProjectEval.objects.get(judge_email=judge.judge_email, project_id=project_id)
        except ObjectDoesNotExist:
            continue

        all_scores_list = all_scores_list + [p.dp_a, p.dp_b, p.dp_c, p.dp_d, p.dp_e, p.dp_f, p.dp_g, p.dp_h, p.p_a, p.p_b, p.p_c, p.p_d]
    n = 0
    for score in all_scores_list:
        if(score == 0):
            continue
        else:
            n += 1
            average_score += score
    if(n > 0):
        average_score /= n
    return round(average_score, 2)

# Function name: makeBool
# Parameters:
#   val - (string) 'true' or 'false'
# Returns: bool
# Description: returns a boolean depending on value of input string
def makeBool(val):
    if val == 'true':
        return True
    return False
