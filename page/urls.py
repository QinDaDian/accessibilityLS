from django.urls import path

from page.views import views

app_name = 'page'
urlpatterns = [
    path('', views.index, name='index'),
    path(r'rule/', views.rule, name='rule'),
    path(r'login/<userid>/', views.login, name='login')

]