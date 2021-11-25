from rest_framework import permissions
from profiles.models import Profiles



class CreateUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            #Check permission for read only request
            return True
        else:
            # Check permission for write request
            # if this username already exists in the Profiles Db, means this user
            # already has a profile, thus creating another one is NOT allowed.
            if Profiles.objects.filter(username=request.user.username).exists():
                return False
            else:
                return True
            