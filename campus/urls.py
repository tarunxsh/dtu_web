from django.urls import path,include
from .views import index,about,newpost,post_detail,post_publish,post_draft_list,post_remove,post_edit

urlpatterns = [
    path('',index,name='index'),
    path('about/', about ,name='about'),
    path('post/new', newpost ,name='newpost'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<pk>/publish/', post_publish, name='post_publish'),
    path('drafts/', post_draft_list, name='post_draft_list'),
    path('post/<pk>/remove/',post_remove, name='post_remove'),
    path('post/<pk>/edit/',post_edit, name='post_edit'),

]
