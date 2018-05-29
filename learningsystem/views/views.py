import json

from django.http import JsonResponse
from django.shortcuts import render

from page.models import Rule, Page
from learningsystem.models import Item, Record


def ruleList(request):
    rule_list = Rule.objects.filter(implemented=1).order_by('rule_id')
    context = {
        'rule_list': rule_list,
    }
    return render(request, 'rule_list.html', context)


# 获取用户学习开始前选择的rule
ruleids=[]
def getRuleIds(request):
     global ruleids
     if request.method == 'POST':
        user_obj = json.loads(request.body.decode())
        ruleids = user_obj.get('ruleIds')
        resultstatus = 'sucess'
        if len(ruleids)!=0:
            return JsonResponse(resultstatus, safe=False)


def study(request):
    print(ruleids)
    # 规则筛选
    items = Item.objects.filter(rule_id__in=ruleids)
    item = items[0]

    page = Page.objects.filter(page_id=item.page_id)
    rule_list = Rule.objects.filter(rule_id__in=ruleids)[:7]
    rule = Rule.objects.get(pk=4)
    context = {
        'item': item,
        'page': page,
        'rule_list': rule_list,
        'rule': rule,
    }
    print(context.get('page'))
    return render(request, 'study_task.html', context)


def loading_iframe(request):
    return render(request, 'iframe.html')


# 考试
def exam(request):
    list = map(str, range(25))
    return render(request, 'exam.html', {'list':list})


# 提交学习记录
def submitLearn(request):
    record = Record.objects.create(
        page_id=1,
        rule_id=1,
        user_id=1,
        std_result=1,
        user_result=request.POST['radioCheckResult'],
        reason='test',
        reason_images='test',
        change_count=1,
        judge=1,
    )
    record.save()
    return JsonResponse("success", safe=False)
