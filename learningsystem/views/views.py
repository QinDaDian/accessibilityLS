from django.shortcuts import render

from page.models import Rule,Page
from learningsystem.models import Item
# Create your views here.
from django.db import connection, transaction

def  ruleList(request):
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM page_rule WHERE baz = %s", [self.baz])
    # row = cursor.fetchone()
    # rule_list = Rule.objects.order_by('rule_id')
    rule_list = Rule.objects.filter(implemented=1).order_by('rule_id')
    context = {
        'rule_list': rule_list,
    }
    return render(request, 'rule_list.html', context)


def  study(request):
    page = Page.objects.get(pk = 1)
    rule_list = Rule.objects.filter(implemented=1)[:7]
    context = {
        'page': page,
        'rule_list': rule_list,
    }
    return render(request, 'study_task.html', context)


def  loading_iframe(request):
    return render(request, 'iframe.html')


#模拟考试（暂未实现）
def mockExam(request):
    list = map(str, range(25))
    return render(request,'mockExam.html', {'list':list})

