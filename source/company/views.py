import json
import django_filters

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from rest_framework import filters
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# status codes => http://www.django-rest-framework.org/api-guide/status-codes/
from rest_framework import status

from .serializers import CompanySerializer, DynamicCompanySerializer
from .models import Company


class CompanyList(APIView):    
    def get(self, request, format=None):
        companies = Company.objects.all()

        kwargs = {} #defining an empty set
        param_key = 'fields'
        if param_key in request.query_params.keys():
            val = set(request.query_params[param_key].split(","))
            kwargs[param_key] = val
        
        default_page_size = 10
        param_key = 'page_size'
        page_size = default_page_size
        if param_key in request.query_params.keys():
            val = request.query_params[param_key]
            page_size = val

        default_page_no = 1
        param_key = 'page_no'
        page_no = default_page_no
        if param_key in request.query_params.keys():
            val = request.query_params[param_key]
            page_no = val

        try:
            paginator = Paginator(companies, page_size)
        except ValueError:
            page_size = default_page_size
            paginator = Paginator(companies, page_size)

        try:
            companies_page = paginator.page(page_no)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            page_no = default_page_no
            companies_page = paginator.page(page_no)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results by paginator.page(paginator.num_pages) or emply result can be returned
            companies_page = []

        serializer = DynamicCompanySerializer(companies_page, many=True, **kwargs)
        res_data = {
            "current_count": len(companies_page.object_list),
            "page_size": page_size,
            "page_no": page_no,
            "total_pages": paginator.num_pages,
            "list" : serializer.data
        }
        return Response(res_data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# class CompanyDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Company.objects.get(pk=pk)
#         except Company.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         company = self.get_object(pk)
#         company = CompanySerializer(company)
#         return Response(company.data)

#     def put(self, request, pk, format=None):
#         company = self.get_object(pk)
#         serializer = CompanySerializer(company, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#     def delete(self, request, pk, format=None):
#         company = self.get_object(pk)
#         company.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     # http://www.django-rest-framework.org/api-guide/serializers/#partial-updates
#     def patch(self, request, pk):
#         company = self.get_object(pk)
#         serializer = DynamicCompanySerializer(company, data=request.data, partial=True) # set partial=True to update a data partially
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)