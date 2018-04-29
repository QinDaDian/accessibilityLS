from django.urls import path

from learningsystem.views import views

app_name = 'learningsystem'
urlpatterns = [
    path('ruleList/', views.ruleList, name='ruleList'),
    path('studyIndex/', views.study, name='study'),
    path('loading_iframe/', views.loading_iframe, name='loading_iframe'),
    path('test/', views.test, name='test'),
    path('mockExam/', views.mockExam, name='mockExam'),

]