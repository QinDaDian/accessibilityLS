import datetime

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

import random

from accessibilityLS import settings
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

# //图片上传
def swfUpload(request):
    primaryKey=request.POST.get('primaryKey')  # 获取文件唯一标识符
    upload_file = request.FILES.getlist('file')
    print(upload_file[0])
    for img in upload_file:
        file_suffix = img.name.split(".")[-1]  #后缀
        curr_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") #获取当前时间
        newName = curr_time + '.'+file_suffix
        fname = '%s/upload/%s' % (settings.MEDIA_ROOT, newName)
        with open(fname, 'wb') as pic:
            for f in img.chunks():
                pic.write(f)
            pic.close()
    return HttpResponse("sucess")


