from django.shortcuts import render

# Create your views here.
def  index(request):
    return render(request, 'index.html')


def  rule(request):
    return render(request, 'rule.html')