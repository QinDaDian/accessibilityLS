import datetime
import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import random

from accessibilityLS import settings
from page.models import Rule, Page
from learningsystem.models import Item, Record

IMGs = []   #上传的图片
ruleids=[]

def ruleList(request):
    rule_list = Rule.objects.filter(implemented=1).order_by('rule_id')
    context = {
        'rule_list': rule_list,
    }
    return render(request, 'rule_list.html', context)
# 获取用户学习开始前选择的rule


def study(request):
    global ruleids
    if request.method=="POST":
       ruleids=request.POST.getlist('checkchild')
    # 规则筛选
    pages = Page.objects.all()
    page = random.sample(list(pages),1)[0]
    # items = Item.objects.filter(page_id=page.page_id, rule_id__in=ruleids)
    rule_list = Rule.objects.filter(rule_id__in=ruleids)[:7]
    context = {
        'page': page,
        'rule_list': rule_list,
    }
    return render(request, 'study_task.html', context)


def loading_iframe(request):
    return render(request, 'iframe.html')


# 提交学习记录
@csrf_exempt
def submit_learn(request):
    global IMGs
    imgs = ','.join(IMGs)
    if request.is_ajax():
        arg = json.loads(request.body.decode('utf-8'))
        item = Item.objects.filter(page_id=arg['pageID'], rule_id=arg['ruleID'])
        if item:
            std_result = item.result
            text_reason=item.text_reason
        else:
            std_result = 2
            text_reason='不存在'
            Record.objects.create(
                page_id=arg['pageID'],
                rule_id=arg['ruleID'],
                user_id=1,
                std_result=std_result,
                user_result=arg['userResult'],
                reason=arg['userReason'],
                reason_images=imgs,
                change_count=arg['chooseCount'],
                judge=1 if std_result == arg['userResult'] else 0,
        )
        result = {
            "stdReason": text_reason,
            "std_result": std_result,
            'resultStatus': 'SUCESS'
        }
    return JsonResponse(result, safe=False)

    #切换学习项
@csrf_exempt
def changeitem(request):
    if request.is_ajax():
        arg = json.loads(request.body.decode('utf-8'))
        print(arg)
        rule=Rule.objects.filter(rule_id=arg['ruleID'])
        record = Record.objects.filter(page_id=arg['pageID'], rule_id=arg['ruleID'], user_id=1)
        item = Item.objects.filter(page_id=arg['pageID'], rule_id=arg['ruleID'])
        result = {
            "rule": rule,
            "record": record,
            "item": item
        }
        return JsonResponse(result, safe=False)


# //图片上传
@csrf_exempt
def swfUpload(request):
    global IMGs
    upload_file = request.FILES.get('file')
    file_suffix = upload_file.name.split(".")[-1]  #后缀
    curr_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") #获取当前时间
    newName = 'upload/'+ curr_time + '.'+file_suffix
    IMGs.append(newName)
    fname = '%s/%s' % (settings.MEDIA_ROOT, newName)
    with open(fname, 'wb') as pic:
        for f in upload_file.chunks():
            pic.write(f)
        pic.close()
    return HttpResponse("sucess")

