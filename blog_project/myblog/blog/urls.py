from myblog.blog.views import PostDetailView, PostListView, PostUpdateView
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

URLPatterns = [
  path(r'^$',views.PostListView(),name='post_lists')
  path(r'^about/$',views.AboutView.as_view(),name='about'),
  path(r'^post/?p<pk>\d+)$'),views.PostDetailView.as_view(),name='post_detail'),
  path(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
  path(r'^post/(?<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit')
  
]