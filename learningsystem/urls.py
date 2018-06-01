from django.urls import path

from learningsystem.views import views

app_name = 'learningsystem'
urlpatterns = [
    path('ruleList/', views.ruleList, name='ruleList'),
    path('studyIndex/', views.study, name='study'),
    path('loading_iframe/', views.loading_iframe, name='loading_iframe'),
    path('swfUpload/', views.swfUpload, name='swfUpload'),
    path('submitLearn', views.submitLearn, name='submitLearn')
]