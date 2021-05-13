from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django_test import models


# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/user-list/',
        'Details View': '/user-list/<str:pk>/',
        'Create': '/user-create/',
        'Update': '/user-update/<str:pk>/',
        'Delete': '/user-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def userList(request):
    reg = models.Register.objects.all()
    serializer = RegisterSerializer(reg, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    reg = models.Register.objects.get(uid=pk)
    serializer = RegisterSerializer(reg, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def userCreate(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def userUpdate(request, pk):
    reg = models.Register.objects.get(uid=pk)
    serializer = RegisterSerializer(instance=reg,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def userDelete(request, pk):
    reg = models.Register.objects.get(uid=pk)
    reg.delete()
    return Response('Item successfully deleted....')