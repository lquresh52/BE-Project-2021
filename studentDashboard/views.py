from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from adminPanel.serializers import QuestionSerializer , TestSerializer
from adminPanel.models import *
from django.http import HttpResponse, JsonResponse
from studentDashboard.models import  Exam_History
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

        # print(request.user)

        test = Test.objects.get(id=subject_id)
        tot_questions = test.totalQuestions
        print(tot_questions)
        
        # will store the subject id 
        history_data = dict()
        history_data["subject_id"] = int(subject_id)
        history_data["selected_op_for_que"] = list()
        # history_data['selected_op_for_que'].append({'que_no':1, 'selcted_op': 2})
        # history_data['selected_op_for_que'].append({'que_no':2, 'selcted_op': 2})
        # history_data['selected_op_for_que'].append({'que_no':3, 'selcted_op': 2})
        # history_data['selected_op_for_que'].append({'que_no':4, 'selcted_op': 2})

        print('------------')
        print(history_data)
        print('------------')

        selected_op = []
        data = request.POST.get('data')
        
        print(type(data))
        print(data)
        print("----------")
        data = json.loads(data) 
        print(type(data))
        print(data[0]['fields'])

        # looping to get selected option
        for i in range(1,tot_questions+1):
            op = int(request.POST.get(f'selected-op-{i}'))
            selected_op.append(op)

        print(selected_op)

        # calculating result
        score = 0
        for i in range(len(selected_op)):
            history_data['selected_op_for_que'].append({"que_no": data[i]['fields']['question_number'], "selcted_op": selected_op[i]})
            correct_ans = int(data[i]['fields']['answer'])
            if correct_ans == selected_op[i]:
                score += 1

        print(score)

        print('------ history data ------')
        print(history_data)
        print('------------')

        # TODO : First need to check if user has already given the test or not if not create new Exam_history obj else update in the old record

        # soring in Exam history model that user has given this test    
        history = Exam_History.objects.create(user=request.user, test_id=test, score=score, no_of_que=tot_questions, right_ans=score, wrong=(tot_questions-score), selected_ans=history_data)
        print('------ history data stored id  ------')
        print(history.id)
        print('---------------')

        # pass the data and score to result page and total number of ques
        return redirect(result_page,score = score, tot_ques = tot_questions, history_id = history.id)
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



def result_page(request,score,tot_ques,history_id):

    history = Exam_History.objects.get(id=history_id)
    selected_op = history.selected_ans
    print(selected_op)
    print(history)

    questions = Question.objects.filter(subject = history.test_id.id)
    ques = list(questions)
    data = serializers.serialize("json",ques)
    print('------old data')
    print(data)
    print('======//////////===')

    data = json.loads(data) 
    print('88888888888888888888888')
    print(type(data))
    


    for i in range(1,history.test_id.totalQuestions+1):
        print(i)
        for op in selected_op['selected_op_for_que']:
            if op['que_no'] == i:
                print(op['selcted_op'])
                print('yes')
                data[i-1]["fields"]["selected_option"] = op["selcted_op"]
                break
            # else:
                # data[i]["fields"]["selected_option"] = op["selcted_op"]

    print('--------final data')
    print(data)
    print('=====end')

    if request.method == "POST":
        return render(request,"studentDashboard/result.html")
    else:
        tot_ques_lst = [int(i) for i in range(tot_ques)]
        percentage = round((score / len(tot_ques_lst)) * 100, 2)
        return render(request,"studentDashboard/result.html", context={'data':data,'tot_ques_lst':tot_ques_lst,'len':len(tot_ques_lst),'score':score, 'history':history, 'percentage': percentage})




def historyPage(request):
    history = Exam_History.objects.filter(user=request.user)
    print(history)
    return render(request,"studentDashboard/history_page.html", context={'history':history})
