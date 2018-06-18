from datetime import datetime
import json

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import random
from accessibilityLS import settings
from page.models import Rule, Page
from learningsystem.models import Item, Record
from utils.decorator import authentication


# 获取用户学习开始前选择的rule
@authentication
def ruleList(request):
    rule_list = Rule.objects.filter(implemented=1).order_by('rule_id')
    context = {
        'rule_list': rule_list,
    }
    return render(request, 'rule_list.html', context)


@authentication
def study(request):
    if request.method=="POST":
        ruleids = request.POST.getlist('checkchild')
        request.session['ruleids'] = ruleids
    else:
        ruleids = request.session.get('ruleids')
    # 规则筛选
    pages = Page.objects.all()
    page = random.sample(list(pages), 7)
    if len(ruleids) == 0:
        rule_list = random.sample(list(Rule.objects.all()), 7)[0]
    else:
        rule_list = Rule.objects.filter(rule_id__in=ruleids)[:7]
    items = Item.objects.filter(page_id=page.page_id, rule_id__in=ruleids)
    context = {
        'items': items,
        'page': page,
        'rule_list': rule_list,
    }
    return render(request, 'study_task.html', context)


@authentication
def loading_iframe(request):
    return render(request, 'iframe.html')


# 提交学习记录
@csrf_exempt
@authentication
def submit_learn(request):
    imgs = ','.join(request.session.get('IMGs'))
    if request.is_ajax():
        arg = json.loads(request.body.decode('utf-8'))
        item = Item.objects.filter(page_id=arg['pageID'], rule_id=arg['ruleID'])
        print(arg["start_time"])     # 2018/6/4 21:40:24
        start_time = datetime.strptime(arg["start_time"], "%Y/%m/%d %H:%M:%S")
        start_time = datetime.strftime(start_time, "%Y-%m-%d %H:%M:%S")
        if item:
            std_result = item.result
            text_reason = item.text_reason
        else:
            std_result = 2
            text_reason = '不存在'
            Record.objects.create(
                page_id=arg['pageID'],
                rule_id=arg['ruleID'],
                user_id=request.session.get('username'),
                std_result=std_result,
                user_result=arg['userResult'],
                reason=arg['userReason'],
                reason_images=imgs,
                change_count=arg['chooseCount'],
                judge=1 if std_result == arg['userResult'] else 0,
                start_time=start_time,
                create_time=start_time,
            )
            # 存下图片路径后删除session
            del request.session['IMGs']
        result = {
            "stdReason": text_reason,
            "std_result": std_result,
            'resultStatus': 'SUCCESS'
        }
    return JsonResponse(result, safe=False)


# 切换学习项
def change_item(request):
    if request.is_ajax():
        arg = json.loads(request.body.decode('utf-8'))
        rule =Rule.objects.filter(rule_id=arg['ruleID'])
        record = Record.objects.filter(page_id=arg['pageID'], rule_id=arg['ruleID'], user_id=1)
        item = Item.objects.filter(page_id=arg['pageID'], rule_id=arg['ruleID'])
        result = {
            "rule": tojson(rule),
            "record": tojson(record),
            "item": tojson(item)
        }
        return JsonResponse(result, safe=False)


# //图片上传
@csrf_exempt
@authentication
def swfUpload(request):
    upload_file = request.FILES.get('file')
    file_suffix = upload_file.name.split(".")[-1]  #后缀
    curr_time = datetime.now().strftime("%Y%m%d%H%M%S%f") #获取当前时间
    newName = 'upload/'+ curr_time + '.'+file_suffix
    fname = '%s/%s' % (settings.MEDIA_ROOT, newName)
    with open(fname, 'wb') as pic:
        for f in upload_file.chunks():
            pic.write(f)
        pic.close()

    # 图片路径存入session
    IMGs = request.session.get('IMGs', False)
    if IMGs is False:
        IMGs = [newName]
    else:
        IMGs.append(newName)
    request.session['IMGs'] = IMGs
    return HttpResponse("success")


def tojson(queryset):
    queryset=serialize("json", queryset, ensure_ascii=False)
    return queryset
