from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from adminPanel.serializers import QuestionSerializer , TestSerializer
from adminPanel.models import *
from django.http import HttpResponse, JsonResponse

@login_required(login_url='/login/')
def dashboard(request):
    tests = Test.objects.filter(quiz_completed=True)
    print(tests)
    return render(request, 'studentDashboard/dashboard.html',{'tests':tests})


def studentTest(request,subject_id):
    testSubject = subject_id
    print("Test ID: ",testSubject)
    ques = Question.objects.filter(subject = subject_id)
    ques_json = QuestionSerializer(ques, many=True)
    print(ques_json.data)
    # return JsonResponse(ques_json.data, safe=False)
    return render(request,"studentDashboard/student_test_page.html",context={'question':ques_json.data})