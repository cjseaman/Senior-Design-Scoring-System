#views.py
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from scoringsystem import forms
from scoringsystem import models as m

def projectEvalView(request):
    return render(request, 'projects_eval_form.html')

def submittedProjectEvalView(request):
    submitProjectEval(request)
    return render(request, 'submitted.html')

@csrf_exempt
def submitProjectEval(request):
    if request.method == 'POST':
        form = forms.ProjectEvalForm(request.POST)
        if form.is_valid():
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
            econ_consideration = request.POST.get("econ_consideration")
            envi_consideration = request.POST.get("envi_consideration")
            sust_consideration = request.POST.get("sust_consideration")
            manu_consideration = request.POST.get("manu_consideration")
            ethi_consideration = request.POST.get("ethi_consideration")
            heal_consideration = request.POST.get("heal_consideration")
            soci_consideration = request.POST.get("soci_consideration")
            poli_consideration = request.POST.get("poli_consideration")
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
            score.save()
            return render(request, 'submitted.html')
    else:
        form = forms.TestScoreForm()

    return render(request,'error.html')
