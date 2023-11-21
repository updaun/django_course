import jwt
from datetime import datetime, timedelta
from django.conf import settings
import random
import string
from users.models import User

def get_random(length):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))

def get_access_token(payload):
    return jwt.encode(
        {"exp": datetime.now() + timedelta(minutes=5), **payload},
        settings.SECRET_KEY,
        algorithm="HS256",
    )
    
def get_refresh_token(payload):
    return jwt.encode(
        {"exp": datetime.now() + timedelta(minutes=5), "data": get_random(10)},
        settings.SECRET_KEY,
        algorithm="HS256",
        
    )
    
def decodeJWT(bearer):
    
    if not bearer:
        return None
    
    token = bearer[7:]
    try:
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
    except jwt.exceptions.ExpiredSignatureError:
        return "expired"
    except jwt.exceptions.DecodeError:
        return "decode_error"
    
    if decoded:
        try:
            return User.objects.get(id=decoded.get("user_id"))
        except User.DoesNotExist:
            return None
        