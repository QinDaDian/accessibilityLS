from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from page.models import Rule, Page


def  gettip(request):
    return render(request, 'exam_tip.html')

def exam(request):
    page = Page.objects.all()[1]
    rule_list = Rule.objects.filter(implemented=1)[:7]
    rule = rule_list[0]
    list = map(str, range(25))
    context = {
        'page': page,
        'rule_list': rule_list,
        'rule': rule,
        'list': list,
    }
    return render(request, 'exam.html', context)

  # //初始化页面时将已学习过的条目字体设为红色
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

