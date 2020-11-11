from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    help_dict = {'help_dict':'This is the Help Page'}
    return render(request, 'appTwo/index.html',context=help_dict)
