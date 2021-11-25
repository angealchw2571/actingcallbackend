#-----------------------------------------------------
# rest_frameworks
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
#-----------------------------------------------------
# local files import - Models
from forums.models import Posts, Discussion
#-----------------------------------------------------
# local files import - Serializers
from forums.api.serializers import PostsSerializer, DiscussionSerializer
#-----------------------------------------------------
# local files import - Permissions
from forums.api.permissions import ReviewPostOrReadOnly, ReviewDiscussionOrReadOnly
from forums.api.permissionsCreate import CreatePostOrReadOnly, CreateDiscussionOrReadOnly


class PostsAV(APIView):

    permission_classes = [CreatePostOrReadOnly]

    def get(self, request):
        print(request.user.id)
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        
        
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        posts = Posts.objects.all()
        self.check_object_permissions(request, posts)
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostsDetailAV(APIView):

    permission_classes = [ReviewPostOrReadOnly]
    
    def get(self, request, pk):
        try:
            posts = Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            return Response({'Posts not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostsSerializer(posts)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def put(self,request,pk):
        posts = Posts.objects.get(pk=pk)
        self.check_object_permissions(request, posts)
        serializer = PostsSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        posts = Posts.objects.get(pk=pk)
        self.check_object_permissions(request, posts)
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-------------------------------------------------------------------

class DiscussionAV(APIView):

    permission_classes = [CreateDiscussionOrReadOnly]

    def get(self, request):
        discussion = Discussion.objects.all()
        serializer = DiscussionSerializer(discussion, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        discussion = Posts.objects.all()
        self.check_object_permissions(request, discussion)
        serializer = DiscussionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiscussionDetailAV(APIView):

    permission_classes = [ReviewDiscussionOrReadOnly]

    def get(self, request, pk):
        try:
            discussion = Discussion.objects.get(pk=pk)
        except Discussion.DoesNotExist:
            return Response({'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DiscussionSerializer(discussion)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def put(self,request,pk):
        discussion = Discussion.objects.get(pk=pk)
        self.check_object_permissions(request, discussion)
        serializer = DiscussionSerializer(discussion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        discussion = Discussion.objects.get(pk=pk)
        self.check_object_permissions(request, discussion)
        discussion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)