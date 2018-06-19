import time
import random

from django.db.models import Count
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from exam.models import Examination, Question
from learningsystem.models import Item
from page.models import Rule, Page


def get_tip(request):
   question_num = Rule.objects.filter(implemented=1).exclude(type=1).aggregate(question_num = Count('rule_id'))
   return render(request, 'exam_tip.html', {'num': question_num['question_num']})

def init_exam(request,questionnum):
    Examination.objects.update_or_create(
        user_id=request.session.get('userid'),
        question_num=questionnum,
        score=0,
        start_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取当前时间
    )
    examid = Examination.objects.all().last().examination_id
    return HttpResponseRedirect('/exam/'+str(examid)+'/1')

def exam(request,examid,questionid):
    print(examid)
    print(questionid)
    # page 和 rule的选择
    rule_list = random.sample(list(Rule.objects.filter(implemented=1).exclude(type=1)), 7)
    print(rule_list)
    page = random.sample(list(Page.objects.all()), 1)
    question_num = 1
    for rule in rule_list:
        item = Item.objects.filter(page_id=page.pageID, rule_id=rule.ruleID)
        Question.objects.create(
            examination_id=exam.examination_id,
            question_number=question_num,
            page_id=page.page_id,
            rule_id=rule.ruleid,
            std_result=item.result,
            std_reason=item.text_reason,
            start_time=exam.start_time
        )
        question_num += 1

    return render(request, 'exam.html')

# def exam(request):
#     page = Page.objects.all()[1]
#     rule_list = Rule.objects.filter(implemented=1)[:7]
#     rule = rule_list[0]
#     list = map(str, range(25))
#     context = {
#         'page': page,
#         'rule_list': rule_list,
#         'rule': rule,
#         'list': list,
#     }
#     return render(request, 'exam.html', context)

  # 初始化页面时将已学习过的条目字体设为红色
def  getdone(request):
    rule_list = Rule.objects.filter(implemented=1)[:7]
    context = {
        'rule_list': rule_list,
    }
    return JsonResponse(context, safe=False)

def  getresult(request):
    return render(request, 'exam_result.html')

# def  getRuleIds(request):
#      global ruleids
#      if request.method == 'POST':
#         user_obj = json.loads(request.body.decode())
#         ruleids = user_obj.get('ruleIds')
#         resultstatus = 'sucess'
#         if len(ruleids)!=0:
#             return JsonResponse(resultstatus, safe=False)

