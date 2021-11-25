#-----------------------------------------------------
# rest_frameworks
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

#-----------------------------------------------------
# local files import - Serializers
from profiles.api.serializers import ProfilesSerializer
#-----------------------------------------------------
# local files import - Models
from profiles.models import Profiles
#-----------------------------------------------------
# local files import - Permissions
from profiles.api.permissions import ReviewUserOrReadOnly
from profiles.api.permissionsCreate import CreateUserOrReadOnly



class ProfilesAV(APIView):

    permission_classes = [CreateUserOrReadOnly]

    def get(self, request):
        profiles = Profiles.objects.all()
        serializer = ProfilesSerializer(profiles, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        profiles = Profiles.objects.all()
        # permissions check here.
        self.check_object_permissions(request, profiles)
        serializer = ProfilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
# for Profiles, filter is done by username instead of id, as it makes it easier for frontend to
# do filtering, since username is forced to be unique as well.
class ProfilesDetailAV(APIView):

    permission_classes = [IsAuthenticated, ReviewUserOrReadOnly]

    def get(self, request, username):
        try:
            profiles = Profiles.objects.get(username=username)
        except Profiles.DoesNotExist:
            return Response({'No such User Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfilesSerializer(profiles)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def put(self,request,username):
        profiles = Profiles.objects.get(username=username)
        # permissions check here. 
        self.check_object_permissions(request, profiles)
        serializer = ProfilesSerializer(profiles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,username):
        profiles = Profiles.objects.get(username=username)
        # permissions check here.
        self.check_object_permissions(request, profiles)
        profiles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




    
