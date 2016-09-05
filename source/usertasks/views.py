from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404
from .serializers import UserSerializer, TaskSerializer, DynamicUserSerializer
from .models import User, Task
from company.models import Company

class DynamicFields(object):
    """A mixins that allows the query builder to display certain fields"""

    def get_fields_to_display(self):
        fields = self.request.GET.get('fields', None)
        return fields.split(',') if fields else None

    def get_serializer(self, instance=None, data=None, files=None, many=False,
                       partial=False, allow_add_remove=False):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        context = self.get_serializer_context()
        fields = self.get_fields_to_display()
        return serializer_class(instance, data=data, files=files,
                                many=many, partial=partial,
                                allow_add_remove=allow_add_remove,
                                context=context, fields=fields)

    def get_pagination_serializer(self, page):
        """
        Return a serializer instance to use with paginated data.
        """
        class SerializerClass(self.pagination_serializer_class):
            class Meta:
                object_serializer_class = self.get_serializer_class()

        pagination_serializer_class = SerializerClass
        context = self.get_serializer_context()
        fields = self.get_fields_to_display()
        return pagination_serializer_class(instance=page, context=context, fields=fields)


class DynamicUserList(DynamicFields, APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = DynamicUserSerializer(users, many=True)
        return Response(serializer.data)


class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, user_pk, format=None):
        user = self.get_object(user_pk)
        user = UserSerializer(user)
        return Response(user.data)

    def put(self, request, user_pk, format=None):
        user = self.get_object(user_pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_pk, format=None):
        user = self.get_object(user_pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskList(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    # def get_object(self, pk):
    #     try:
    #         return User.objects.get(pk=pk)
    #     except Company.DoesNotExist:
    #         raise Http404

    def get(self, request, user_pk, task_pk, format=None):
        # user = self.get_object(user_pk)
        # user = UserSerializer(user)
        return Response(status.HTTP_200_OK)

    # def put(self, request, user_pk, format=None):
    #     user = self.get_object(user_pk)
    #     serializer = UserSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, user_pk, format=None):
    #     user = self.get_object(user_pk)
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
