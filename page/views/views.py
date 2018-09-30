from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from utils.decorator import authentication


# Create your views here.
@authentication
def index(request):
    # return render(request, 'index.html')
    return HttpResponseRedirect(reverse('learningsystem:ruleList'))

@authentication
def rule(request):
    return render(request, 'rule.html')


def login(request, userid):
    print(userid)
    request.session['userid'] = userid
    return HttpResponseRedirect(reverse('learningsystem:ruleList'))
