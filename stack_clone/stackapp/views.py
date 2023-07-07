from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
# Create your views here.
class UserviewSet(viewsets.ViewSet):
    def create(self,request):
        ser=UserSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"created"})
        return Response ({"msg":"faild"})