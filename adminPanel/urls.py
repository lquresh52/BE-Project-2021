from django.urls import path
from . import views
urlpatterns = [
    path('',views.teacherHome,name='teacherHome'),
    path('questionForm/',views.questionForm,name="questionForm"),
    path('questionList/<int:quiz_id>/<int:totalQuestions>/',views.questionList,name="questionList"),
    # path('questionList/<quiz>/<subjectName>/<totalQuestions>/<totalMarks>/<dateTime>/<examDuration>/<negativeMarksInput>/',views.questionList,name="questionList"),
]
