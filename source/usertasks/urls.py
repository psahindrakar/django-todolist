from django.conf.urls import include, url
from .views import UserList, UserDetail, TaskList, TaskDetail

urlpatterns = [
    url( r'^$', UserList.as_view(), name = 'User list' ),
    url( r'^(?P<user_pk>[0-9]+)/$', UserDetail.as_view(), name = 'User detail' ),
    url( r'^(?P<user_pk>[0-9]+)/tasks/$', TaskList.as_view(), name = 'Task list' ),
    url( r'^(?P<user_pk>[0-9]+)/tasks/(?P<task_pk>[0-9]+)/$', TaskDetail.as_view(), name = 'Task details' ),
]