from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/',views.signUp,name='signup'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('password-reset/', views.password_reset, name='password-reset'),
    path('password-reset-completed/<uidb64>/', views.password_reset_completed, name='password-reset-completed'),
    path('password-reset-confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password-reset-confirm'),
]
