from django.urls import re_path, include,path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TasklistCreateView,TasklistDetailsView,TaskCreateView,TaskDetailsView,TagCreateView,TagDetailsView,OwnerCreateView,OwnerDetailsView,TaskUpdateView
from rest_framework.authtoken.views import obtain_auth_token
from todolist.views import Register
from .import views



# http://127.0.0.1:8000/todolists/2/tasks/2/update

urlpatterns = {

    re_path('auth', include('django.contrib.auth.urls')),

    re_path('register/', Register.as_view(), name='register'),

    re_path('home', views.tasks_home, name ='home'),

    re_path('create', views.create, name ='create'),
     
    re_path('<int:pk>/update', views.TaskUpdateView.as_view(), name ='task-update'),

  


    re_path(r'^todolistsOwnerC/$', OwnerCreateView.as_view(), name="Owner"),
    re_path(r'^todolistsOwnerD/(?P<pk>[0-9]+)/$', OwnerDetailsView.as_view(), name="Owner-detail"),

    re_path(r'^todolistsTag/$', TagCreateView.as_view(), name="Tag"),
    re_path(r'^todolistsTagD/(?P<pk>[0-9]+)/$', TagDetailsView.as_view(), name="Tag-detail"),
    re_path(r'^todolists/(?P<list_id>[0-9]+)/tasks', TaskCreateView.as_view(), name="tasks"),
    re_path(r'^todolists/(?P<list_id>[0-9]+)/tasks/(?P<pk>[0-9]+)', TaskDetailsView.as_view(), name="task-detail"),

    
    re_path(r'^todolists13/$', TaskCreateView.as_view(), name="delete"),
    re_path(r'^todolists12/(?P<pk>[0-9]+)/$', TaskDetailsView.as_view(), name="detail"),
    re_path(r'^todolists/$', TasklistCreateView.as_view(), name="lists"),
    re_path(r'^todolists/(?P<pk>[0-9]+)/$', TasklistDetailsView.as_view(), name="list-detail"),
    
}

urlpatterns = format_suffix_patterns(urlpatterns)