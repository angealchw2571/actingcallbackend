from rest_framework import serializers
from casts.models import Castcall

class CastCallSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Castcall
        fields = "__all__"