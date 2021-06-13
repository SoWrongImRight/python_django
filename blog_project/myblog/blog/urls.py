from django.urls import path
from django.urls.resolvers import URLPattern
from blog import views

URLPatterns = [URLPattern
  path(r'^about/$',views.AboutView.as_view(),name='about'),
  
]