from rest_framework import serializers
from users.models import User

class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    name = serializers.CharField(required = False)
    email = serializers.EmailField(required = False)
    phone_number = serializers.CharField(required = False)
    password = serializers.CharField(min_length=8)
    password2 = serializers.CharField(min_length=8)
    
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("이미 존재하는 아이디입니다.")
        return value
    
    def validate_phone_number(self, value):
        return "".join(i for i in value if i.isdigit())
    
    def validate(self, data):
        password = data.get("password")
        password2 = data.get("password2")
        if password != password2:
            raise serializers.ValidationError("두 비밀번호가 일치하지 않습니다.")
        return data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
        