from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from page.models import Rule


def  gettip(request):
    return render(request, 'exam_tip.html')

def exam(request):
    list = map(str, range(25))
    return render(request, 'exam.html', {'list':list})

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

