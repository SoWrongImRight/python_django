from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   return HttpResponse("<em>My second project</em>")



def help(request):
    help_dict = {'help_insert':'This is the Help Page'}
    return render(request, 'appTwo/appTwo.html',context=help_dict)
