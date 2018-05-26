from django.urls import path

from exam import views

app_name = 'exam'
urlpatterns = [
    path('tip/', views.gettip, name='tip'),
    path('/', views.exam, name='exam'),
    path('examResult/', views.getresult, name='examResult'),

]