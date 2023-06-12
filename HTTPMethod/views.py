from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.files import File
#from .models import Employee
#from .serializer import *
# Create your views here.


class FileOperation(APIView):
    def get(self, request ,path):
        f = open(path, 'r')
        contents = f.read()
        return Response(contents, status=status.HTTP_201_CREATED)

    def post(self, request, path):
        f = open(path, 'a')
        testfile = File(f)
        #result = 'my name is yogesh'
        result = request.data
        testfile.write(result)
        testfile.close
        f.close
        return Response(result, status=status.HTTP_201_CREATED)






# # Create your views here.
# class EmployeeView(APIView):
#     def get(self,request):
#         obj=Employee.objects.all()
#         serializer =EmployeeSerializer(obj, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self,request):
#         serializer=EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
#
# class EmployeeInfo(APIView):
#     # def get(self,request,id):
#     #     try:
#     #         obj=Employee.objects.get(id=id)
#     #     except Employee.DoesNotExist:
#     #         msg={'msg':'record not found'}
#     #         return Response(msg, status=status.HTTP_404_NOT_FOUND)
#     #     serializer =EmployeeSerializer(obj)
#     #     return Response(serializer.data,status=status.HTTP_200_OK)
#
#     def put(self,request,id):
#         try:
#             obj=Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#             msg = {'msg': 'record not found'}
#             return Response(msg, status=status.HTTP_404_NOT_FOUND)
#         serializer = EmployeeSerializer(obj,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self,request,id):
#         try:
#             obj=Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#             msg = {'msg': 'record not found'}
#             return Response(msg, status=status.HTTP_404_NOT_FOUND)
#         serializer = EmployeeSerializer(obj,data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,id):
#         try:
#             obj=Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#             msg={'msg':'record not found'}
#             return Response(msg,status=status.HTTP_404_NOT_FOUND)
#
#         obj.delete()
#         return Response({'msg':'deleted'}, status=status.HTTP_204_NO_CONTENT)

