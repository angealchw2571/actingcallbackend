from rest_framework import serializers
from profiles.models import Profiles
from casts.api.serializers import CastCallSerializer


class ProfilesSerializer(serializers.ModelSerializer):

    casts = CastCallSerializer(many=True, read_only=True)

    class Meta:
        model = Profiles
        fields = "__all__"
        
