from django.urls import path

from exam import views

app_name = 'exam'
urlpatterns = [
    path('tip/', views.get_tip, name='tip'),
    path(r'initExam/<questionnum>', views.init_exam, name='initexam'),
    path(r'<examid>/<questionid>/', views.exam, name='exam'),
    path('examResult/', views.getresult, name='getresult'),
    path('getdone/', views.getdone, name='getdone'),

]