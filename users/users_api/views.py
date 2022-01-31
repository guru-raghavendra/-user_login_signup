import email
from django.shortcuts import render
from pip import main

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import detailsSerializer,loginSerializer
from .models import userDetails

class signup(APIView):
    def post(self, request):
        serializer = detailsSerializer(data=request.data)
        
        if serializer.is_valid():
            mail=serializer.initial_data['email']
            
            if(userDetails.objects.filter(email=mail).count()==0):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data['name']+" already exist... try loging in", status=status.HTTP_409_CONFLICT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class login(APIView):
    def post(self, request):
        serializer = loginSerializer(data=request.data)

        if serializer.is_valid():
            mail=serializer.initial_data['email']
            password=serializer.initial_data['password']
            
            if(userDetails.objects.filter(email=mail).count()==0):
                return Response(serializer.data['email']+" user does not exist... try sign up", status=status.HTTP_404_NOT_FOUND)
            
            if(userDetails.objects.get(email=mail).password== password):
                name=userDetails.objects.get(email=mail).name
                return Response(name+" login successful!!", status=status.HTTP_200_OK) 
            else:
                return Response("invalid credentials", status=status.HTTP_400_BAD_REQUEST) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

