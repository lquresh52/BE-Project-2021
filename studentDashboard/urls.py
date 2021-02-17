from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('studentTest/<str:subject_id>/',views.studentTest,name="studentTest"),
    path('historyPage',views.historyPage,name='historyPage'),
    path('result-page/<int:score>/<int:tot_ques>/<str:data>/',views.result_page,name='result-page'),
]
