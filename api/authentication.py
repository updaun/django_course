from rest_framework.permissions import BasePermission

class IsAuthenticatedCustom(BasePermission):
    
    def has_permission(self, request, view):
        from users.utils import decodeJWT
        
        user = decodeJWT(request.META.get("HTTP_AUTHORIZATION"))
        
        # unusual
        if user == "expired" or user == "decode_error" or user is None:
            return False
        
        # usual
        
        request.user = user
        if request.user and request.user.is_authenticated:
            return True
        return False
        
        
