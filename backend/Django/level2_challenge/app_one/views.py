from django.shortcuts import render

# Create your views here.
def index(request):
    index_dict = {'index_insert':'Go to /users to see a list of users'}
    return render(request, 'app_one/index.html',context=index_dict)

def users(request):
    user_dict = {'user_list':'replace with table of users info'}
    return render(request, 'app_one/users.html',context=user_dict)