import json

from django.http import  JsonResponse
from django.shortcuts import render

from page.models import Rule,Page


def  ruleList(request):
    rule_list = Rule.objects.filter(implemented=1).order_by('rule_id')
    context = {
        'rule_list': rule_list,
    }
    return render(request, 'rule_list.html', context)

# 获取用户学习开始前选择的rule
ruleids=[]
def  getRuleIds(request):
     global ruleids
     if request.method == 'POST':
        user_obj = json.loads(request.body.decode())
        ruleids = user_obj.get('ruleIds')
        resultstatus = 'sucess'
        if len(ruleids)!=0:
            return JsonResponse(resultstatus, safe=False)

def  study(request):
    print(ruleids)
    page = Page.objects.all()[1]
    rule_list = Rule.objects.filter(implemented=1)[:7]
    rule = Rule.objects.get(pk = 4)
    context = {
        'page': page,
        'rule_list': rule_list,
        'rule': rule,
    }
    print(context.get('page'))
    return render(request, 'study_task.html', context)

def  loading_iframe(request):
    return render(request, 'iframe.html')


#考试
def exam(request):
    list = map(str, range(25))
    return render(request, 'exam.html', {'list':list})
