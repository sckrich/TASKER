from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers, generics
from .models import User, Group, Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class UserSerializer(serializers.Serializer):
    class Meta:
        model: User
        fields = "__all__"
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
     
        token['username'] = user.username
        token['email'] = user.user_email
        token['user_id'] = user.user_id
        
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        
        user = self.user
        data.update({
            'user_id': user.user_id,
            'username': user.username,
            'email': user.user_email,
            'first_name': user.first_name,
            'last_name': user.last_name
        })
        return data