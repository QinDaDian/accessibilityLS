from django.shortcuts import render

# Create your views here.


def  ruleList(request):
    return render(request, 'rule_list.html')


def  study(request):
    return render(request, 'study_task.html')

def  loading_iframe(request):
    return render(request, 'iframe.html')
