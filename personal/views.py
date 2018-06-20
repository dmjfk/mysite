from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    # return render(request, 'personal/details.html',{'content':['Want to contact me, please email me.','dmjfk170@gmail.com']})
    return render(request, 'personal/details.html')
