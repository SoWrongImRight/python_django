from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpattern = [
    path('',views.SchoolListView.as_view(),name='list'),
    path(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
]