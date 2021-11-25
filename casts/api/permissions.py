from rest_framework import permissions
from profiles.models import Profiles


class ReviewCastOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            #Check permision for read only request
            return True
        else:
            # Check permisson for write request
            # find linked profile id
            object_id = obj.postedBy_id
            
            # using this profile id, find the relevant profile.
            findUserId = Profiles.objects.get(pk=object_id)
            
            # using this profile's foreign key, accountLinked, we
            # find the relevant user id which is linked. 
            # we compare this relevant user id, and check if it tally
            # with current log in user id.
            return findUserId.accountLinked_id == request.user.id

            