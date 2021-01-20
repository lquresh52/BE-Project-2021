from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('studentTest/<str:subject_id>/',views.studentTest,name="studentTest"),
]
