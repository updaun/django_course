from rest_framework.views import APIView
from users.serializers import SignupSerializer, LoginSerializer
from users.models import User, Jwt
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from users.utils import get_access_token, get_refresh_token

class SignupAPI(APIView):
    serializer_class = SignupSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.pop("password2")
        user = User.objects.create_user(
            **serializer.validated_data
        )
        return Response(status = status.HTTP_201_CREATED, data={"message":"회원가입이 완료되었습니다."})


class LoginAPI(APIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        user = authenticate(
            request,
            username=serializer.validated_data.get("username"),
            password=serializer._validated_data.get("password"),
        )
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"message":"입력하신 정보가 올바르지 않습니다."})
        
        
        # jwt token remove
        Jwt.objects.filter(user=user).delete()
        
        # jwt token 발급
        access = get_access_token({"user_id":user.id})
        refresh = get_refresh_token()
        
        
        access = get_access_token({"user_id":user.id})
        refresh = get_refresh_token()
        
        Jwt.objects.create(
            user=user,
            accesss=access,
            refresh=refresh,
        )
        
        login(request, user)
        
        response = Response(status=status.HTTP_200_OK)
        data = {
            "access":access,
        }
        response.data = data
        response.set_cookie(key="access", value=access)
        response.set_cookie(key='refresh', value=refresh, httponly=True)
        
        return response
    
class LogoutAPI(APIView):
    def get(self, request):
        
        # jwt token remove
        from users.utils import decodeJWT
        user = decodeJWT(request.META.get("HTTP_AUTHORIZATION"))
        if user != "expired" and user != "decode_error" and user is not None:
            Jwt.objects.filter(user=user).delete()
        
        # session logout
        logout(request)
        
        # cookie remove
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        
        return response