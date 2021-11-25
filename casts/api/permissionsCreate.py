from rest_framework import permissions



class CreateCastOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            #Check permission for read only request
            return True
        else:
            if request.user.id:
                return True
            else:
                return False