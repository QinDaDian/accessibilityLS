import json

from django.http import  JsonResponse
from django.shortcuts import render

from page.models import Rule,Page


def  loading_iframe(request):
    return render(request, 'iframe.html')

def  ruleList(request):
    rule_list = Rule.objects.filter(implemented=1).order_by('rule_id')
    context = {
        'rule_list': rule_list,
    }
    return render(request, 'rule_list.html', context)

# 获取用户学习开始前选择的rule
ruleids=[]

def  study(request):
    ruleids =request.POST.getlist('checkchild')
    print(ruleids)
    page = Page.objects.all()[1]
    rule_list = Rule.objects.filter(implemented=1)[:7]
    rule = rule_list[0]
    context = {
        'page': page,
        'rule_list': rule_list,
        'rule': rule,
    }
    return render(request, 'study_task.html', context)




