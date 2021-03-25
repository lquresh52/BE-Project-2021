from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from . models import Test,Question
from django.contrib.auth.models import User
from studentDashboard.models import Exam_History
from studentDashboard.views import result_page
from django.core import serializers
from adminPanel.serializers import QuestionSerializer , TestSerializer

import json

question_increment = 0

@login_required(login_url='/login/')
def teacherHome(request):
    tests = Test.objects.filter(quiz_completed=True)
    print(tests)

    if request.method == 'POST':
        test_id = request.POST.get('testIdHidden')
        print(test_id)
        delete_test = Test.objects.filter(id=test_id)
        delete_test.delete()

    return render(request,'adminPanel/teacher_dashboard.html',{'tests':tests})

@login_required(login_url='/login/')
def questionForm(request):
    user = request.user
    print(user)
    if request.method == 'POST':
        subjectName = request.POST.get('subjectName')
        branch = request.POST.get('branchSelect')
        year = request.POST.get('yearSelect')
        totalQuestions = request.POST.get('totalQuestions')
        totalMarks = request.POST.get('totalMarks')
        dateTime = request.POST.get('dateTime')
        examDuration = int(request.POST.get('examDuration'))*60
       # negativeMarksInput = request.POST.get('negativeMarksInput')
        #print("Neg mark  ",negativeMarksInput)
        quiz = Test(user=user,subjectName=subjectName,branch_field=branch,year_field=year,totalQuestions=totalQuestions,totalMarks=totalMarks,dateTime=dateTime,examDuration=examDuration)
      #  print("Neg mark 2 ",negativeMarksInput)
        quiz.save()
        # tp = Test.objects.get(pk=quiz.pk)
        print('*********************************************')
        print(quiz)
        print('----------------------------------------')
        print(quiz.pk)
        print('///////////  ',quiz.totalQuestions)

        # return redirect(questionList,quiz=quiz,subjectName=subjectName,totalQuestions=totalQuestions,totalMarks=totalMarks,dateTime=dateTime,examDuration=examDuration,negativeMarksInput=0 if negativeMarksInput==''else negativeMarksInput)
        return redirect(questionList,quiz_id=quiz.pk,totalQuestions=quiz.totalQuestions,curr_q_no=1)
    else:
        return render(request,'adminPanel/newquestion.html')

# def questionList(request,quiz,subjectName,totalQuestions,totalMarks,dateTime,examDuration,negativeMarksInput):
    # print(subjectName)
@login_required(login_url='/login/')
def questionList(request,quiz_id,totalQuestions,curr_q_no):
    
    quiz = Test.objects.get(id=quiz_id)
    print(quiz)
    if request.method == 'POST':

        
        question = request.POST.get('question')
        if question == "":
            question = request.POST.get('question_img')
        
        op1 = request.POST.get('option1')
        if op1 == "":
            op1 = request.POST.get('option1_img')

        op2 = request.POST.get('option2')
        if op2 == "":
            op2 = request.POST.get('option2_img')

        op3 = request.POST.get('option3')
        if op3 == "":
            op3 = request.POST.get('option3_img')

        op4 = request.POST.get('option4')
        if op4 == "":
            op4 = request.POST.get('option4_img')

        answer = request.POST.get('answer')
        que_type = request.POST.get('que_type')
        print("QUES_TYPE",type(que_type))
        desc_answer = request.POST.get('danswer')
        print("DANS",desc_answer)

        # try:
        #     get_que = Question.objects.get(subject=quiz,question_number=curr_q_no)
        #     get_que.question = question
        #     if que_type == 'True':

        #         get_que.is_objective = True
        #         print("GETQUE.",get_que.is_objective)
        #         get_que.option1 = op1
        #         get_que.option2 = op2
        #         get_que.option3 = op3
        #         get_que.option4 = op4
        #         get_que.answer = answer
        #     else:
        #         get_que.is_objective = False
        #         print("GETQUE2345.",get_que.is_objective)
        #         get_que.descriptive_answer = desc_answer
        #     print(get_que.is_objective)
        #     get_que.save()
        # except:
        print("new question")
        if que_type == 'True':
            save_question = Question(subject = quiz,question_number=curr_q_no ,question=question, option1 = op1, option2 = op2, option3 = op3, option4 = op4, answer=answer,is_objective=True,descriptive_answer=None)
        else:
            save_question = Question(subject = quiz,question_number=curr_q_no ,question=question,is_objective=False,descriptive_answer=desc_answer)


        save_question.save()

        if curr_q_no != totalQuestions:
            quiz.number_of_question_added = curr_q_no
            quiz.save() 
            next_q_no = curr_q_no + 1
            return redirect(questionList, quiz_id=quiz.id, totalQuestions=quiz.totalQuestions, curr_q_no=next_q_no)
        else:
            quiz.number_of_question_added = curr_q_no
            quiz.quiz_completed = True
            quiz.save()
            return redirect(teacherHome)
            
    else:
        try:
            get_que = Question.objects.get(subject=quiz,question_number=curr_q_no)
            # print(get_que)
            print('Back------')
        except:
            print("Error")
        return render(request,'adminPanel/newquestion.html',{'question_increment':question_increment})

@login_required
def view_result(request,tid):
    print(tid)
    attempted_exam = Exam_History.objects.filter(test_id = tid)
    print(len(attempted_exam))
    return render(request,'adminPanel/view_result.html', {'exam_history': attempted_exam})
