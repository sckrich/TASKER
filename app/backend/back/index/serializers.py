from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers, generics
from .models import User, Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Добавляем кастомные поля в токен
        token['username'] = user.username
        token['email'] = user.user_email
        token['user_id'] = user.user_id
        
        return token

    def validate(self, attrs):
        # Стандартная валидация
        data = super().validate(attrs)
        
        # Добавляем дополнительные данные в ответ
        user = self.user
        data.update({
            'user_id': user.user_id,
            'username': user.username,
            'email': user.user_email,
            'first_name': user.first_name,
            'last_name': user.last_name
        })
        return data