from rest_framework import permissions


class CreatePostOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            #Check permission for read only request
            return True
        else:
            if request.user.id:
                return True
            else:
                return False

class CreateDiscussionOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            #Check permission for read only request
            return True
        else:
            # to place discussion (comment), need to check if there is a logged in user.
            if request.user.id:
                return True
            else:
                return False