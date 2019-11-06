from django.shortcuts import render
from .scoring_data import Score
import logging

def createscore(request):
    logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
    logging.debug('got to createscore!!')
    if request.method == 'POST':
        if request.POST.get("project_id") and request.POST.get("judge_email")
            score = Score()
            score.project_id = request.POST.get("project_id")
            score.judge_email = request.POST.get("judge_email")
            score.save()
            score.dp_a = request.POST.get("dp_a")
            score.dp_b = request.POST.get("dp_b")
            score.dp_c = request.POST.get("dp_c")
            score.dp_d = request.POST.get("dp_d")
            score.dp_e = request.POST.get("dp_e")
            score.dp_f = request.POST.get("dp_f")
            score.dp_g = request.POST.get("dp_g")
            score.dp_h = request.POST.get("dp_h")
            score.p_a = request.POST.get("p_a")
            score.p_b = request.POST.get("p_b")
            score.p_c = request.POST.get("p_c")
            score.p_d = request.POST.get("p_d")
            econ_consideration = request.POST.get("econ_consideration")
            envi_consideration = request.POST.get("envi_consideration")
            sust_consideration = request.POST.get("sust_consideration")
            manu_consideration = request.POST.get("manu_consideration")
            ethi_consideration = request.POST.get("ethi_consideration")
            heal_consideration = request.POST.get("heal_consideration")
            soci_consideration = request.POST.get("soci_consideration")
            poli_consideration = request.POST.get("poli_consideration")
            comments = request.POST.get("comments")
            score.save()

            return render(request, 'posts/create.html')
    else:
        return render(request, 'posts/create.html')
