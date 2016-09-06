from django.conf.urls import include, url
from .views import CompanyList, CompanyDetail

urlpatterns = [
    url( r'^$', CompanyList.as_view(), name = 'task_list' ),
    url( r'^(?P<pk>[0-9]+)(/)?$', CompanyDetail.as_view(), name = 'task_detail' ),
]