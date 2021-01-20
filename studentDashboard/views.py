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
    if request.method == 'POST':
        # question,option1,option2,option3,option4,answer = []
        question = request.POST.get('question')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        answer = request.POST.get('answer')
        print("Submitted Test: ",question," \n",option1," \n",option2," \n",option3," \n",option4," \n",answer)
        
    else:
        testSubject = subject_id
        print("Test ID: ",testSubject)
        ques = Question.objects.filter(subject = subject_id)
        ques_json = QuestionSerializer(ques, many=True)
        print(ques_json.data)
        print(len(ques_json.data))
    
        # return JsonResponse(ques_json.data, safe=False)
        return render(request,"studentDashboard/student_test_page.html",context={'questions':ques_json.data })
