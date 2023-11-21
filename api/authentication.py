from rest_framework.permissions import BasePermission


class IsAuthenticatedCustom(BasePermission):

    def has_permission(self, request, view):
        from users.utils import decodeJWT

        # JWT 인증
        user = decodeJWT(request.META.get("HTTP_AUTHORIZATION", None))

        # 비정상에 대한 얼리 리턴
        if user == "expired" or user == "decode_error" or user is None:
            return False

        request.user = user
        # 세션인증
        if request.user and request.user.is_authenticated:
            return True
        return False
