# rest_framework related imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# dependent local files imports
from users.api.serializers import RegistrationSerializer, LoginSerializer, TokenSerializer, UserSerializer

# Django in-built user related imports
from django.contrib.auth.models import User
from django.contrib import auth
# from django.contrib.auth import authenticate, login



class LoginViewAV(APIView):

    def post(self,request):

        # serialize user input data to dictionary format
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():

            username = serializer.data['username']
            password = serializer.data['password']
            
            # verify user credentials, user will be None if invalid.
            user = auth.authenticate(request, username=username,password=password)

            if user is not None:
                # backend log in according to the user details
                # saves the user's details in the session
                auth.login(request, user)

                try:
                # filter account details according to the logged in user from User model database
                    accountdetail = User.objects.get(username=username)
                    
                except:
                    return Response({'No such user'}, status=status.HTTP_404_NOT_FOUND)
                
                # serializes this retrieved data, into dictionary format.
                accountserializer = UserSerializer(accountdetail)
                
                # using DRF JWT utility functions to generate a token 
                refresh = RefreshToken.for_user(user)   
                tokenserializer = TokenSerializer(data=
                    {
                        'token': {
                            'refresh': str(refresh),
                            'access': str(refresh.access_token),
                        }
                        
                    })
                tokenserializer.is_valid()
                # frontend require logged in User data and JWT, thus use spread operator to join them and return response.
                login_response = { **accountserializer.data, **tokenserializer.data}
                
                return Response(login_response,status=status.HTTP_200_OK)  

            else: 
                return Response({'Error, incorrect username or password, or account does NOT exist'}, status=status.HTTP_404_NOT_FOUND)     

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutViewAV(APIView):

    def post(self, request):

        if request.data['refresh']:
            # to logout, obtain refresh token and blacklist it.
            current_token = request.data['refresh']
            used_token = RefreshToken(current_token)
            used_token.blacklist()

            # remove the logged in user data in the session
            auth.logout(request)

            return Response({'Logged Out Successfully'},status=status.HTTP_200_OK)

        else:
            return Response({'Error processing request, check refresh token data'}, status=status.HTTP_400_BAD_REQUEST)    

              
class RegistrationViewAV(APIView):

    def post(self,request):

        serializer = RegistrationSerializer(data=request.data)

        # create a new dict, to store register details and feedback to user later.
        data = {}

        if serializer.is_valid():
            account = serializer.save()

         # if successful, access all the details in the account, and store it in data
            data['response'] = "Registration Successful"
            data['username'] = account.username
            data['email'] = account.email
        
        else:
            # errors are dict by itself
            data = serializer.errors


        return Response(data, status=status.HTTP_201_CREATED)   




