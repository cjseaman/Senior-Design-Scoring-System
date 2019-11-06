from django.shortcuts import render
from forms import TestScoreForm
from models import TestScore
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def testSubmitScore(request):
    if request.method == 'POST':
        form = TestScoreForm(request.POST)
        if form.is_valid():
            project_id = request.POST.get("project_id")
            judge_email = request.POST.get("judge_email")
            score = TestScore(project_id=project_id, judge_email=judge_email)
            score.save()
            return HttpResponse("asdfjkl")
    else:
        form = TestScoreForm()

    return render(request,'submitted.html')
