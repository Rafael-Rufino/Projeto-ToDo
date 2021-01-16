from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse('rafael Chegou aqui!')


def taskList(request):
    return render(request, 'tasks/list.html')


def base(request):
    return render(request, './base.html')

    
   
