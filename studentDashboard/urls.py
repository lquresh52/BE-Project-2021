from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('studentTest/<str:subject_id>/',views.studentTest,name="studentTest"),
    path('historyPage',views.historyPage,name='historyPage'),
    path('result-page/<int:score>/<int:history_id>/<int:tot_ques>/',views.result_page,name='result-page'),
    # path('timer/', views.timer_update, name='timer-update'),
]
