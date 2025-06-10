from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User
from rest_framework import status
from django.contrib.auth.hashers import make_password
# Create your views here.
class UserRegistration(viewsets.ViewSet):
    def register(self, request):
        username = request.data.get('username')
        user_password = request.data.get('user_password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        middle_name = request.data.get('middle_name')
        user_email = request.data.get('user_email')
        user_birthdate = request.data.get('user_birthdate')
        if User.objects.filter(user_email = user_email).exists():
            return Response({"error": "Пользователь с таким именем уже существует."}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": "Пользователь с таким именем уже существует."}, status=status.HTTP_400_BAD_REQUEST)
        user = User(first_name = first_name, 
                    last_name = last_name, 
                    middle_name = middle_name, 
                    birth_date = user_birthdate, 
                    username = username, 
                    password = make_password(user_password), 
                    user_email = user_email)
        user.save()
        return Response({"message": "Регистрация успешна!"}, status=status.HTTP_201_CREATED)
class UserLogin(viewsets.ViewSet):
    ...