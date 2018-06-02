import datetime
import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import random

from accessibilityLS import settings
from page.models import Rule, Page
from learningsystem.models import Item, Record

save_tag = 0   #标记记录是否已存在

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
    if request.is_ajax():
        arg = json.loads(request.body.decode('utf-8'))
        if save_tag == 0:
            record = Record.objects.create(
                page_id=arg['pageID'],
                rule_id=arg['ruleID'],
                user_id=1,
                std_result=1,
                user_result=arg['userResult'],
                reason=arg['userReason'],
                reason_images='test',
                change_count=arg['chooseCount'],
                judge=1 if 1 == arg['userResult'] else 0,
            )
            record.save()
        elif save_tag == 1:
            Record.objects.filter(
                page_id=arg['pageID'],
                rule_id=arg['ruleID'],
                user_id=1,
            ).update(
                std_result=1,
                user_result=arg['userResult'],
                reason=arg['userReason'],
                reason_images='test',
                change_count=arg['chooseCount'],
                judge=1 if 1 == arg['userResult'] else 0,
            )
    return JsonResponse({'resultStatus':'FAIL'}, safe=False)

# //图片上传
@csrf_exempt
def swfUpload(request):
    upload_file = request.FILES['file']
    newnamelist=[]
    for img in upload_file:
        file_suffix = img.name.split(".")[-1]  #后缀
        curr_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") #获取当前时间
        newName = 'upload/'+ curr_time + '.'+file_suffix
        newnamelist.append(newName)
        fname = '%s/%s' % (settings.MEDIA_ROOT, newName)
        with open(fname, 'wb') as pic:
            for f in img.chunks():
                pic.write(f)
            pic.close()
    print(','.join(newnamelist))
    # Record.objects.create(
    #     page_id=request.POST.get('pageID'),
    #     rule_id=request.POST.get('ruleID'),
    #     user_result=1,
    #     user_id=1,
    #     std_result=1,
    #     judge=1,
    #     reason_images=','.join(newnamelist),
    # )
    #
    # save_tag =1
    return HttpResponse("sucess")

