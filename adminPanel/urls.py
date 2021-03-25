from django.urls import path
from . import views
urlpatterns = [
    path('',views.teacherHome,name='teacherHome'),
    path('questionForm/',views.questionForm,name="questionForm"),
    path('questionList/<int:quiz_id>/<int:totalQuestions>/<int:curr_q_no>/',views.questionList,name="questionList"),
    path('viewresult/<int:tid>/',views.view_result,name="view_result"),
]
