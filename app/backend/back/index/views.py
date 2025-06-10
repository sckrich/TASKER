from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User
from rest_framework import status
from django.contrib.auth.hashers import make_password
# Create your views here.
class UserRegistration(viewsets.ViewSet):
    def register(self, request):
        user_login = request.data.get('user_login')
        user_password = request.data.get('user_password')
        user_name = request.data.get('user_name')
        user_secname = request.data.get('user_secname')
        user_thname = request.data.get('user_thname')
        user_email = request.data.get('user_email')
        user_birthdate = request.data.get('user_birthdate')
        if User.objects.filter(user_email = user_email).exists():
            return Response({"error": "Пользователь с таким именем уже существует."}, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(viewsets.ViewSet):
    ...