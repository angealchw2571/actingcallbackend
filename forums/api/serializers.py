from rest_framework import serializers
from forums.models import Posts, Discussion
import datetime

now = datetime.datetime.now().replace(microsecond=0)
nowmod = now.strftime("%Y-%m-%d %H:%M:%S")

class DiscussionSerializer(serializers.ModelSerializer):


    class Meta:
        model= Discussion
        fields = "__all__"


class PostsSerializer(serializers.ModelSerializer):

    comments = DiscussionSerializer(many=True, read_only=True)
    

    class Meta:

        model = Posts
        fields = "__all__"
        
        