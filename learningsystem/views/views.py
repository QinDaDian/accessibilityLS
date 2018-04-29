from django.shortcuts import render

from page.models import Rule
# Create your views here.


def  ruleList(request):
    rule_list = Rule.objects.order_by('rule_id')
    context = {
        'rule_list': rule_list,
    }
    return render(request, 'rule_list.html', context)


def  study(request):
    return render(request, 'study_task.html')


def  loading_iframe(request):
    return render(request, 'iframe.html')
