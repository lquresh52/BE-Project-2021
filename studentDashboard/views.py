from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from adminPanel.serializers import QuestionSerializer , TestSerializer
from adminPanel.models import *
from django.http import HttpResponse, JsonResponse

from django.core import serializers

import ast
import random
import json

@login_required(login_url='/login/')
def dashboard(request):
    tests = Test.objects.filter(quiz_completed=True)
    print(tests)
    return render(request, 'studentDashboard/dashboard.html',{'tests':tests})



@login_required(login_url='/login/')
def studentTest(request,subject_id):
    if request.method == 'POST':
        
        test = Test.objects.get(id=subject_id)
        tot_questions = test.totalQuestions
        print(tot_questions)
        selected_op = []
        data = request.POST.get('data')
        print(data)
        print("----------")
        data = json.loads(data) 
        print(type(data))
        print(data[0]['fields'])

        # data = ast.literal_eval(data)
        # print(data)

        for i in range(1,tot_questions+1):
            op = int(request.POST.get(f'selected-op-{i}'))
            selected_op.append(op)

        print(selected_op)
        # calculating result
        score = 0
        for i in range(len(selected_op)):
            correct_ans = int(data[i]['fields']['answer'])
            if correct_ans == selected_op[i]:
                score += 1

        print(score)

        # pass the data and score to result page and total number of ques
        return redirect(result_page,score = score, tot_ques = tot_questions, data = data)
    else:
        testSubject = subject_id
        print("Test ID: ",testSubject)
        ques = Question.objects.filter(subject = subject_id)
        ques = list(ques)
        random.shuffle(ques)
        # ques_json = QuestionSerializer(ques, many=True)
        print(ques)

        # print(ques_json.data)
        # print("------------------")
        data = serializers.serialize("json",ques)
        # print(data)

        
        return render(request,"studentDashboard/student_test_page.html",context={'questions':ques,"data":data })



def result_page(request,score,tot_ques,data):

    data_json = json.dumps(data)
    # print(type(data_json))
    print(data_json[:50])
    # data_json = json.loads(str(list(data_json)))
    # print(type(data_json))
    data_json = list(data_json)
    data_json = json.dumps(data_json)
    print(type(data_json))


    if request.method == "POST":
        return render(request,"studentDashboard/result.html")
    else:
        tot_ques_lst = [i for i in range(tot_ques)] 
        return render(request,"studentDashboard/result.html", context={'data':data_json,'tot_ques_lst':tot_ques_lst,'score':score})




def historyPage(request):
    return render(request,"studentDashboard/history_page.html")
