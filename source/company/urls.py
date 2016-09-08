from django.conf.urls import include, url
from .views import CompanyList, CompanyDetail, CompanyInsuranceFile

urlpatterns = [
    url( r'^$', CompanyList.as_view(), name = 'task_list' ),
    url( r'^(?P<pk>[0-9]+)(/)?$', CompanyDetail.as_view(), name = 'task_detail' ),
    url( r'^(?P<pk>[0-9]+)/insurance_form(/)?$', CompanyInsuranceFile.as_view({'get': 'retrieve'}), name = 'task_detail' ),
]