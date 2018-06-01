import json

from django.http import  JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import random
from page.models import Rule, Page
from learningsystem.models import Item, Record



def ruleList(request):
    rule_list = Rule.objects.filter(implemented=1).order_by('rule_id')
    context = {
        'rule_list': rule_list,
    }
    return render(request, 'rule_list.html', context)
# 获取用户学习开始前选择的rule


def study(request):
    ruleids=request.POST.getlist('checkchild')
    # 规则筛选
    pages = Page.objects.all()
    print(pages)
    page = random.sample(list(pages), 1)[0]
    items = Item.objects.filter(page_id=page.page_id, rule_id__in=ruleids)
    rule_list = Rule.objects.filter(rule_id__in=ruleids)[:7]
    context = {
        'items': items,
        'page': page,
        'rule_list': rule_list,
    }
    return render(request, 'study_task.html', context)


def loading_iframe(request):
    return render(request, 'iframe.html')


# 提交学习记录
@csrf_exempt
def submit_learn(request):
    arg = request.POST['checkResultInfo']
    record = Record.objects.create(
        page_id=arg.pageID,
        rule_id=arg.ruleID,
        user_id=1,
        std_result=1,
        user_result=arg.userResult,
        reason=arg.userReason,
        reason_images='test',
        change_count=arg.chooseCount,
        judge=1 if 1 == arg.userResult else 0,
    )
    record.save()
    return JsonResponse({'resultStatus':'FAIL'}, safe=False)
