# File: urls.py
# Description: This file holds the `urlpatterns` list that routes URLs to view.
#
# For more information please see:
#    https://docs.djangoproject.com/en/2.2/topics/http/urls/

from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project_eval_form/', views.projectEvalView, name='project_eval'),
    path('project_eval_form/submitted', views.submitProjectEval, name='submit_project_eval'),
    path('judge_exp_eval_form/', views.judgeExpEvalView, name='exp_eval'),
    path('judge_exp_eval_form/submitted', views.submitJudgeExpEvalView, name='submit_exp_eval'),
    path('admin_home/', views.adminHomeView, name='admin_home'),
    path('admin_home/scores_summary', views.scoresSummaryView, name='scores_summary'),
    path('admin_home/scores_detail', views.scoresDetailView, name='scores_detail'),
    path('admin_home/sd_experience_results', views.sdExperienceResults, name='sd_experience_results'),
    path('admin_home/sd_experience', views.sdExperience, name='sd_experience'),
    path('admin_home/create_session_form', views.createSessionView, name='create_session'),
    path('admin_home/create_session_form/submitted', views.submittedCreatedSessionView, name='submitted_created_session'),
    path('admin_home/add_judges_form', views.assignJudgesView, name='assign_judges'),
    path('admin_home/add_judges_form/submitted_judge', views.submittedAssignJudgesView, name='submitted_assign_judges'),
    path('admin_home/create_project_form', views.createProjectForm, name='create_project'),
    path('admin_home/create_project_form/submitted', views.submittedCreatedProjectForm, name='submitted_create_project'),
    path('admin_home/delete_session_prompt', views.deleteSessionPromptView, name='delete_session_prompt'),
    path('admin_home/delete_session', views.deleteSessionView, name='delete_session'),
    path('judge_home/', views.judgeHomeView, name='judge_home'),
    path('', views.loginView, name='login'), # home page, default path
    path('login_user/', views.loginUserView, name='login_user'),
    path('logout/', views.logoutView, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')), # login page
]
