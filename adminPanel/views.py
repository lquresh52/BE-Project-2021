from django.shortcuts import render,HttpResponse,redirect
from . models import Test,Question
question_increment = 0
# Create your views here.
def teacherHome(request):
    return render(request,'adminPanel/teacherdash.html')


def questionForm(request):
    user = request.user
    print(user)
    if request.method == 'POST':
        subjectName = request.POST.get('subjectName')
        totalQuestions = request.POST.get('totalQuestions')
        totalMarks = request.POST.get('totalMarks')
        dateTime = request.POST.get('dateTime')
        examDuration = request.POST.get('examDuration')
        negativeMarksInput = request.POST.get('negativeMarksInput')
        
        quiz = Test(user=user,subjectName=subjectName,totalQuestions=totalQuestions,totalMarks=totalMarks,dateTime=dateTime,examDuration=examDuration,negativeMarksInput=0 if negativeMarksInput==''else negativeMarksInput)
        quiz.save()
        # tp = Test.objects.get(pk=quiz.pk)
        print('*********************************************')
        print(quiz)
        print('----------------------------------------')
        print(quiz.pk)
        print('///////////  ',quiz.totalQuestions)

        # return redirect(questionList,quiz=quiz,subjectName=subjectName,totalQuestions=totalQuestions,totalMarks=totalMarks,dateTime=dateTime,examDuration=examDuration,negativeMarksInput=0 if negativeMarksInput==''else negativeMarksInput)
        return redirect(questionList,quiz_id=quiz.pk,totalQuestions=quiz.totalQuestions)
    else:
        return render(request,'adminPanel/question.html')

# def questionList(request,quiz,subjectName,totalQuestions,totalMarks,dateTime,examDuration,negativeMarksInput):
    # print(subjectName)
def questionList(request,quiz_id,totalQuestions):
    global question_increment
    if question_increment<=(int(totalQuestions)):
        question_increment+=1
        if request.method == 'POST':
            question = request.POST['question']
            option1 = request.POST['option1text']
            option2 = request.POST['option2text']
            option3 = request.POST['option3text']
            option4 = request.POST['option4text']
            answer = request.POST['answer']
            difficulty_level = request.POST['difficulty']
            print(question)

            paper = Question(subject=Test.objects.get(pk=quiz_id),question=question,option1=option1,option2=option2,option3=option3,option4=option4,answer=answer,difficulty_level=difficulty_level)
            print("Paper",paper)
            paper.save()

            if int(question_increment)==(int(totalQuestions)+1):
                print('mmmmmmmmmmmmmmmmmmmmmmmm')
                question_increment=0;
                return HttpResponse("<h1>Thank You </h1><h3>Ho gaya bhai</h3>")

            print("Question: "+question+"Option1: "+option1+"Option2: "+option2+"Option 3:"+option3+"Option4: "+option4+"Answer: "+answer,difficulty_level)
            return render(request,'adminPanel/option_list.html',{'question_increment':question_increment})
        else:
            # print("Question List -> "+subjectName,totalQuestions,totalMarks,dateTime,examDuration,negativeMarksInput)
            return render(request,'adminPanel/option_list.html',{'question_increment':question_increment})

    else:
        question_increment=0;
        return HttpResponse("<h1>Thank You </h1><h3>Your Paper is Created</h3>")