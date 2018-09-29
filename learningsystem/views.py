from datetime import datetime
import json

import os

from django.core.serializers import serialize
from django.db import connection
from django.db.models import Q
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
    userid = request.session.get('userid')
    cursor = connection.cursor()
    cursor.execute("""SELECT  pr.*,coalesce(right_num,0) AS right_num,coalesce(wrong_num,0)AS  wrong_num
                   from page_rule pr
                   LEFT JOIN
                   (SELECT rule_id,
                   sum(CASE WHEN judge =1 THEN 1 ELSE 0 END) AS  right_num,
                   sum(CASE WHEN judge =0 THEN 1 ELSE 0 END) AS  wrong_num
                   FROM learningsystem_record
                   WHERE user_id = "+userid+"
                   group by rule_id) lr
                   ON pr.rule_id=lr.rule_id
                   WHERE pr.implemented=1
                   AND pr.type!=1
                   ORDER BY pr.rule_id""")
    list = dictfetchall(cursor)  # 读取所有
    cursor.close()
    context = {
        'list': list,
    }
    return render(request, 'rule_list.html', context)


@authentication
def study(request):
    imgs = request.session.get('IMGs')
    if imgs:
        for img in imgs:
            os.remove('%s/%s' % (settings.MEDIA_ROOT, img))
    request.session['IMGs'] = []
    if request.method == "POST":
        ruleids = request.POST.getlist('checkchild')
        request.session['ruleids'] = ruleids
    else:
        ruleids = request.session.get('ruleids')
    # 规则筛选
    pages = Page.objects.all()
    page = random.sample(list(pages), 1)[0]
    if ruleids:
        rule_list = random.sample(list(Rule.objects.filter(implemented=1).filter(~Q(type=1))), 7)
    else:
        rule_list = random.sample(list(Rule.objects.filter(rule_id__in=ruleids)), 7)
    item = Item.objects.filter(page_id=page.page_id, rule_id=rule_list[0].rule_id)
    rule = Rule.objects.get(rule_id=rule_list[0].rule_id)
    if rule.freq_ans:
        freq_ans = rule.freq_ans.split('#F#G#F#')[:-1]
    else:
        freq_ans = []
    context = {
        'item': item,
        'page': page,
        'rule_list': rule_list,
        'freq_ans': freq_ans,
    }
    return render(request, 'study_task.html', context)


@authentication
def loading_iframe(request):
    return render(request, 'iframe.html')


# 提交学习记录
@csrf_exempt
@authentication
def submit_learn(request):
    # 处理图片存储路径
    if request.session.get('IMGs'):
        imgs = ','.join(request.session.get('IMGs'))
    else:
        imgs = ''

    if request.is_ajax():
        arg = json.loads(request.body.decode('utf-8'))
        item = Item.objects.filter(page_id=arg['pageID'], rule_id=arg['ruleID'])
        start_time = datetime.strptime(arg["start_time"], "%Y/%m/%d %H:%M:%S")
        start_time = datetime.strftime(start_time, "%Y-%m-%d %H:%M:%S")
        if item:
            std_result = item[0].result
            text_reason = item[0].text_reason
        else:
            std_result = 2
            text_reason = '不存在'
        Record.objects.create(
            page_id=arg['pageID'],
            rule_id=arg['ruleID'],
            user_id=request.session.get('userid'),
            std_result=std_result,
            user_result=arg['userResult'],
            reason=arg['userReason'],
            reason_images=imgs,
            change_count=arg['chooseCount'],
            judge=1 if std_result == arg['userResult'] else 0,
            start_time=start_time,
        )
        # 存下图片路径后删除session
        request.session['IMGs'] = []
        result = {
            "stdReason": text_reason,
            "std_result": std_result,
            'resultStatus': 'SUCCESS'
        }
    return JsonResponse(result, safe=False)


# 切换学习项
def change_item(request):
    if request.is_ajax():
        imgs = request.session['IMGs']
        if imgs:
            for img in imgs:
                os.remove('%s/%s' % (settings.MEDIA_ROOT, img))
        request.session['IMGs'] = []
        arg = json.loads(request.body.decode('utf-8'))
        rule = Rule.objects.filter(rule_id=arg['ruleID'])
        record = Record.objects.filter(page_id=arg['pageID'], rule_id=arg['ruleID'],
                                       user_id=request.session.get('userid'))
        item = Item.objects.filter(page_id=arg['pageID'], rule_id=arg['ruleID'])
        if rule[0].freq_ans:
            freq_ans = rule[0].freq_ans.split('#F#G#F#')[:-1]
        else:
            freq_ans = []
        result = {
            "rule": tojson(rule),
            "record": tojson(record),
            "item": tojson(item),
            'freq_ans': freq_ans
        }
        return JsonResponse(result, safe=False)


# //图片上传
@csrf_exempt
@authentication
def swfUpload(request):
    upload_file = request.FILES.get('file')
    file_suffix = upload_file.name.split(".")[-1]  # 后缀
    curr_time = datetime.now().strftime("%Y%m%d%H%M%S%f")  # 获取当前时间
    newName = 'upload/' + curr_time + '.' + file_suffix
    if not os.path.exists(settings.MEDIA_ROOT + '/upload'):
        os.makedirs(settings.MEDIA_ROOT + '/upload')
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
    print(request.session['IMGs'])
    return HttpResponse("success")


def tojson(queryset):
    queryset = serialize("json", queryset, ensure_ascii=False)
    return queryset


def dictfetchall(cursor):
    # 将游标返回的结果保存到一个字典对象中
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]