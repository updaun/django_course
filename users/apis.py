from rest_framework.views import APIView
from users.serializers import SignupSerializer
from users.models import User
from rest_framework.response import Response
from rest_framework import status


class SignupAPI(APIView):
    serializer_class = SignupSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.pop("password2")
        User.objects.create_user(
            **serializer.validated_data
        )
        return Response(status=status.HTTP_201_CREATED, data={"message":"회원가입이 완료되었습니다."})
    