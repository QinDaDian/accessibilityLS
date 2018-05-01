from django.shortcuts import render

from page.models import Rule,Page
from learningsystem.models import Item
# Create your views here.


def  ruleList(request):
    rule_list = Rule.objects.filter(implemented = 1)
    context = {
        'rule_list': rule_list,
    }
    return render(request, 'rule_list.html', context)


def  study(request):
    page = Page.objects.get(pk = 1)
    context = {
        'page': page,
    }
    return render(request, 'study_task.html', context)


def  loading_iframe(request):
    return render(request, 'iframe.html')


#模拟考试（暂未实现）
def mockExam(request):
    list = map(str, range(25))
    return render(request,'mockExam.html', {'list':list})


def  test(request):
    return render(request, 'www.baidu.com')
