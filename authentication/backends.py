from django.contrib.auth.hashers import check_password

from .models import UserToDo
from django.db.models import Q


class AuthBackend(object):
    def get_user(self, user_id):
        try:
            return UserToDo.objects.get(pk=user_id)
        except:
            return None

    def authenticate(self, request, email, password):
        try:
            user = UserToDo.objects.get(Q(email=email))
        except:
            return None
        return user if check_password(password, user.password) else None