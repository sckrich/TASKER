from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User, Group
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



class UserGroups(viewsets.ViewSet):
    def getGroups(self, request):
        permission_classes = [IsAuthenticated]
        authentication_classes = [JWTAuthentication]
        user_id = request.data.get("user_id")
        user = User.objects.get(user_id = user_id)
        groups = Group.objects.filter(user = user_id)
        groups_serializer = GroupSerializer(groups, many = True)
        return Response({"groups": groups_serializer.data}, status = status.HTTP_200_OK)
    
class UserRegistration(viewsets.ViewSet):
    def register(self, request):
        print(request.data)
        first_name = request.data.get('first_name')
        username = request.data.get('username')
        user_password = request.data.get('user_password')
        last_name = request.data.get('last_name')
        middle_name = request.data.get('middle_name')
        user_email = request.data.get('user_email')
        user_birthdate = request.data.get('user_birthdate')
        if User.objects.filter(user_email = user_email).exists():
            return Response({"error": "Пользователь с таким именем уже существует."}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": "Пользователь с таким именем уже существует."}, status=status.HTTP_400_BAD_REQUEST)
        user = User(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            birth_date=user_birthdate,
            username=username,
            password=make_password(user_password),
            user_email=user_email
        )
        user.save()
        return Response({"message": "Регистрация успешна!"}, status=status.HTTP_201_CREATED)
class UserLogin(viewsets.ViewSet):
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('user_password')
        try:
            if User.objects.filter(username = username).exists():
                user = User.objects.get(username=username)
                if(check_password(password, user.password)):
                    return Response({
                       "status":"success",
                    })
                else:
                    return Response({"error": "Неверный пароль"}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)