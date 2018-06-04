from django.urls import path

from learningsystem import views

app_name = 'learningsystem'
urlpatterns = [
    path(r'ruleList/', views.ruleList, name='ruleList'),
    path(r'studyIndex/', views.study, name='study'),
    path(r'loading_iframe/', views.loading_iframe, name='loading_iframe'),
    path(r'swfUpload/', views.swfUpload, name='swfUpload'),
    path(r'submit_learn/', views.submit_learn, name='submit_learn'),
    path(r'changeitem/', views.changeitem, name='changeitem')
]