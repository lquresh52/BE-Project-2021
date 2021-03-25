from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from adminPanel.serializers import QuestionSerializer , TestSerializer
from adminPanel.models import *
from django.http import HttpResponse, JsonResponse
from studentDashboard.models import  Exam_History, Time_Tracker
from django.core import serializers


import ast
import random
import json
import nltk
# import gensim
import numpy as np

from nltk.tokenize import word_tokenize, sent_tokenize

avg_sims = []


@login_required(login_url='/login/')
def dashboard(request):
    historys = Exam_History.objects.filter(user=request.user,is_test_given=True)
    history_ids = [ history.test_id.id for history in historys]
    print(history_ids)
    tests = Test.objects.filter(quiz_completed=True).exclude(id__in=history_ids)
    #print(tests)
    # for test in tests:
    #     print("test",test)
    # print("HIST",history)
    return render(request, 'studentDashboard/dashboard.html',{'tests':tests})



@login_required(login_url='/login/')
def studentTest(request,subject_id):
    if request.method == 'POST':

        # #print(request.user)

        test = Test.objects.get(id=subject_id)
        tot_questions = test.totalQuestions
        #print(tot_questions)
        
        # will store the subject id 
        history_data = dict()
        history_data["subject_id"] = int(subject_id)
        history_data["selected_op_for_que"] = list()
        # history_data['selected_op_for_que'].append({'que_no':1, 'selcted_op': 2})
        # history_data['selected_op_for_que'].append({'que_no':2, 'selcted_op': 2})
        # history_data['selected_op_for_que'].append({'que_no':3, 'selcted_op': 2})
        # history_data['selected_op_for_que'].append({'que_no':4, 'selcted_op': 2})

        #print('------------')
        #print(history_data)
        #print('------------')

        selected_op = []
        data = request.POST.get('data')
        
        #print(type(data))
        #print(data)
        #print("----------")
        data = json.loads(data) 
        #print(type(data))
        # print(data)

        # looping to get selected option
        for i in range(1,tot_questions+1):
            if request.POST.get(f'question-type-{i}') == 'True':
                op = int(request.POST.get(f'selected-op-{i}'))
            else:
                op = request.POST.get(f'selected-op-{i}')
            print(op)
            selected_op.append(op)

        print(selected_op)

        # calculating result
        score = 0

        for i in range(len(selected_op)):
            history_data['selected_op_for_que'].append({"que_no": data[i]['fields']['question_number'], "selcted_op": selected_op[i]})
            print(type(data[i]['fields']['is_objective']))
            if data[i]['fields']['is_objective'] == True:
                correct_ans = int(data[i]['fields']['answer'])
                if correct_ans == selected_op[i]:
                    score += 1
            else:
                print(str(data[i]['fields']['descriptive_answer']))
        #         gen_docs = sent_tokenize(str(data[i]['fields']['descriptive_answer']))
        #         gen_docs = [ [w.lower() for w in word_tokenize(text)] for text in gen_docs ]

        #         dictionary = gensim.corpora.Dictionary(gen_docs)
        #         corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs ]
        #         tf_idf = gensim.models.TfidfModel(corpus)
        #         sims = gensim.similarities.Similarity('workdir/', tf_idf[corpus], num_features=len(dictionary))

        #         file2_docs = sent_tokenize(selected_op[i])

        #         for line in file2_docs:
        #             query_doc = [w.lower() for w in word_tokenize(line)]
        #             query_doc_bow = dictionary.doc2bow(query_doc)
        #             query_doc_tf_idf = tf_idf[query_doc_bow]
        #             print('Comparing Result:', sims[query_doc_tf_idf]) 
        #             sum_of_sims =(np.sum(sims[query_doc_tf_idf], dtype=np.float32))
        #             avg = sum_of_sims / len(gen_docs)
        #             print(f'avg: {sum_of_sims / len(gen_docs)}')
        #             avg_sims.append(avg)

        #         total_avg = np.sum(avg_sims, dtype=np.float)
        #         print(total_avg)
        #         percentage_of_similarity = round(float(total_avg) * 100)
        #         if percentage_of_similarity >= 100:
        #             percentage_of_similarity = 100
        #         if percentage_of_similarity >= 50:
        #             score += 1 
        #         print(percentage_of_similarity, score)

              
            

        # print(score)

        #print('------ history data ------')
        #print(history_data)
        #print('------------')

        # TODO : First need to check if user has already given the test or not if not create new Exam_history obj else update in the old record

        # soring in Exam history model that user has given this test
        try:
            history = Exam_History.objects.get(user=request.user, test_id=test)
            print("PREVHIST",history)
            history.score = score
            history.right_ans = score
            history.wrong=(tot_questions-score)
            history.selected_ans=history_data
            history.save()
        except:
            history = Exam_History.objects.create(user=request.user, test_id=test, score=score, no_of_que=tot_questions, right_ans=score, wrong=(tot_questions-score), selected_ans=history_data, is_test_given=True)
        #print('------ history data stored id  ------')
        #print(history.id)
        #print('---------------')

        # pass the data and score to result page and total number of ques
        return redirect(result_page,score = score, tot_ques = tot_questions, history_id = history.id)
  
    elif request.is_ajax():
        time = request.GET.get('time','')
        print('///////////////')
        print(time)

        test_id = request.GET.get('test_id','')

        test_object = Test.objects.get(id=test_id)

        user = request.user

    
        if Time_Tracker.objects.filter(user=user, test_id=test_object).exists():
            tracker = Time_Tracker.objects.get(user=user,test_id = test_object)
            
            tracker_time = time.split(':')
            print(tracker_time)
            hour = tracker_time[0].strip()
            minute = tracker_time[1].strip()
            sec = tracker_time[2].strip()

            print("Minute",minute)
            updated_time = int(hour) * 3600 + int(minute) * 60 + int(sec)
            
            tracker.time_left = updated_time
            
            tracker.save()
        else:
            tracker = Time_Tracker.objects.create(user=user, test_id=test_object, time_left=time)  
            tracker.save()
            tp = Time_Tracker.objects.get(test_id=test_object, user=user)
            print(tp.time_left,'*************')  


        # resp = {
        #     'updatedTime' : new_time,
        # }
        # print(new_time)
        # response = json.dumps(resp)
        return HttpResponse(content_type="application/json")

    else:
        testSubject = subject_id
        print("Test ID: ",testSubject)
        test = Test.objects.get(id = testSubject)

        # Time Tracker Object
        tracker_obj = Time_Tracker.objects.filter(user= request.user , test_id=test).exists()
        
        print("Exists: ",tracker_obj)

        if tracker_obj:
            tracker_time_left = Time_Tracker.objects.get(user=request.user, test_id=test).time_left
        else:
            tracker_time_left = None

        ques = Question.objects.filter(subject = subject_id)
        ques = list(ques)
        random.shuffle(ques)
        # ques_json = QuestionSerializer(ques, many=True)
        #print(ques)

        # #print(ques_json.data)
        # #print("------------------")
        data = serializers.serialize("json",ques)
        # #print(data)

        
        return render(request,"studentDashboard/student_test_page.html",context={'questions':ques,"data":data, "test":test,"tracker_exists":tracker_obj,"tracker_time": tracker_time_left })


# def timer_update(request):
#     if request.method == 'POST':
#         time = request.POST.get('time','')
#         print('///////////////')
#         print(time)
#         print('///////////////')
#         return HttpResponse("H gaya")


def result_page(request,score,history_id,tot_ques,):
    print(score,history_id,tot_ques)
    history = Exam_History.objects.get(user=request.user,id= history_id)
    selected_op = history.selected_ans
    #print(selected_op)
    print("HISTORY",history)

    questions = Question.objects.filter(subject = history.test_id.id)
    ques = list(questions)
    data = serializers.serialize("json",ques)
    #print('------old data')
    #print(data)
    #print('======//////////===')

    data = json.loads(data) 
    #print('88888888888888888888888')
    #print(type(data))
    


    for i in range(1,history.test_id.totalQuestions+1):
        #print(i)
        for op in selected_op['selected_op_for_que']:
            if op['que_no'] == i:
                #print(op['selcted_op'])
                #print('yes')
                data[i-1]["fields"]["selected_option"] = op["selcted_op"]
                break
            # else:
                # data[i]["fields"]["selected_option"] = op["selcted_op"]

    #print('--------final data')
    #print(data)
    ##print('=====end')

    if request.method == "POST":
        return render(request,"studentDashboard/result.html")
    else:
        tot_ques_lst = [int(i) for i in range(tot_ques)]
        percentage = round((score / len(tot_ques_lst)) * 100, 2)
        return render(request,"studentDashboard/result.html", context={'data':data,'tot_ques_lst':tot_ques_lst,'len':len(tot_ques_lst),'score':score, 'history':history, 'percentage': percentage})




def historyPage(request):
    history = Exam_History.objects.filter(user=request.user)
    #print(history)
    return render(request,"studentDashboard/history_page.html", context={'history':history})
