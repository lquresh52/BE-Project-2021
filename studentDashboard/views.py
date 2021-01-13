from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from adminPanel.models import Test,Question

@login_required(login_url='/login/')
def dashboard(request):
    tests = Test.objects.filter(quiz_completed=True)
    print(tests)
    return render(request, 'studentDashboard/dashboard.html',{'tests':tests})


def studentTest(request,subjectName):
    testSubject = subjectName
    print("Test ID: ",testSubject)
    ques = Question.objects.filter(subjectName = testSubject)
    print("Questions: ",ques.question, " Option1: ",ques.option1," Option2 ",ques.option2, "Option3: ",ques.option3,"Option4: ",ques.option4,"Answer: ",ques.answer,"Question Number: ",ques.question_number )
    
    return render(request,"studentDashboard/student_test_page.html")