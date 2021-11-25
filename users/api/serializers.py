from django.contrib.auth.models import User
from rest_framework import serializers
from profiles.api.serializers import ProfilesSerializer
import re

# Serializer for Login -------------------------------

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    

# Serializer for Issuing Tokens -------------------------------

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)

# Serializer for Login Data Response to FrontEnd -------------------------------

class UserSerializer(serializers.ModelSerializer):

    profiles = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User
        # fields = "__all__"
        fields = ['username', 'email', 'id', 'profiles']


# Serializer for Registration of Account -------------------------------

class RegistrationSerializer(serializers.ModelSerializer):

    # use fields if we don't want to utilise all the attributes in the defined Model.
    class Meta:
        model = User
        fields = ['username', 'email','password']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def save(self):


        password = self.validated_data['password']
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        # Check if:
        # username / email already exists
        # length of username and password must be greater than 6
        # valid email input

        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error': 'Sorry, username is taken.'})

        elif User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists!'})
        
        elif len(self.validated_data['username']) < 6 or len(self.validated_data['password']) < 6:
            raise serializers.ValidationError({'error': 'Username and Password must be at least 6 characters long!'})

        elif (not (re.fullmatch(regex, self.validated_data['email']))):
            raise serializers.ValidationError({'error': 'Not a valid email!'})


        # if checks are ok, pass username, email and password into accounts, which is referring to the User model.
        account = User(email=self.validated_data['email'], username= self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account


