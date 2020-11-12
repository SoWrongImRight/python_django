from django.shortcuts import render
from app_one.models import app_users

# Create your views here.
def index(request):
    index_dict = {'index_insert':'Go to /users to see a list of users'}
    return render(request, 'app_one/index.html',context=index_dict)

def users(request):
    user_records = app_users.objects.order_by('fname')
    user_dict = {"user_list":user_records}
    return render(request, 'app_one/users.html',context=user_dict)