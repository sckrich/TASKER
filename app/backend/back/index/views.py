from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User, Group, Task
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, GroupSerializer, TaskSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserTasksList(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def getTasks(self, request):
        
        user_id = request.data.get("user_id")
        tasks = Task.objects.filter(assigned_user = user_id)
        tasks_serializer = TaskSerializer(tasks, many = True)
        return Response({"tasks": tasks_serializer.data}, status = status.HTTP_200_OK)
    
class UserGroups(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def getGroups(self, request):
        
        user_id = request.data.get("user_id")
        user = User.objects.filter(user_id = user_id)
        groups = Group.objects.filter(user = user_id)
        groups_serializer = GroupSerializer(groups, many = True)
        return Response({"groups": groups_serializer.data}, status = status.HTTP_200_OK)
    
class UserRegistration(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]
    def register(self, request):
        first_name = request.data.get('first_name')
        username = request.data.get('username')
        user_password = request.data.get('user_password')
        last_name = request.data.get('last_name')
        middle_name = request.data.get('middle_name')
        user_email = request.data.get('user_email')
        user_birthdate = request.data.get('user_birthdate')
        if User.objects.filter(user_email = user_email).exists():
            return Response({"error": "User alredy exists."}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": "User alredy exists."}, status=status.HTTP_400_BAD_REQUEST)
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
        return Response({"message": "registrated"}, status=status.HTTP_201_CREATED)
    
class UserLogin(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('user_password')
        try:
            if User.objects.filter(username = username).exists():
                user = User.objects.get(username=username)
                if(check_password(password, user.password)):
                    refresh = RefreshToken.for_user(user) 
                    access_token = str(refresh.access_token)
                    return Response({
                        "access": access_token,
                        "refresh": str(refresh),
                        "user_id": user.user_id,
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"error": "User undefined"}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"error": "User undefined"}, status=status.HTTP_404_NOT_FOUND)