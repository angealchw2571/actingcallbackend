#-----------------------------------------------------
# rest_frameworks
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#-----------------------------------------------------
# local files import - Serializers
from casts.api.serializers import CastCallSerializer
#-----------------------------------------------------
# local files import - Models
from casts.models import Castcall
from profiles.models import Profiles
#-----------------------------------------------------
# local files import - Permissions
from casts.api.permissions import ReviewCastOrReadOnly
from casts.api.permissionsCreate import CreateCastOrReadOnly


class CastCallAV(APIView):
    
    permission_classes = [CreateCastOrReadOnly]

    def get(self, request):
        
        castcall = Castcall.objects.all()
        serializer = CastCallSerializer(castcall, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        profiles = Profiles.objects.all()
        # permission check here
        self.check_object_permissions(request, profiles)
        serializer = CastCallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            

class CastCallDetailAV(APIView):

    permission_classes = [ReviewCastOrReadOnly]

    def get(self, request, pk):
        
        try:
            castcall = Castcall.objects.get(pk=pk)
        except Castcall.DoesNotExist:
            return Response({'No such cast call'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CastCallSerializer(castcall)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        
        castcall = Castcall.objects.get(pk=pk)
        # permission check here
        self.check_object_permissions(request, castcall)
        serializer = CastCallSerializer(castcall, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        castcall = Castcall.objects.get(pk=pk)
        # permission check here
        self.check_object_permissions(request, castcall)
        castcall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)