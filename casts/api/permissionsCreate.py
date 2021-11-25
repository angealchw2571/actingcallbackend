from rest_framework import permissions



class CreateCastOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            #Check permission for read only request
            return True
        else:
            # basically, to create cast, check if user.id exists, as this indicates there is a user logged in.
            if request.user.id:
                return True
            else:
                return False