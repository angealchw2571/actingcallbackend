# allows access to token, when uer and pw is sent
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from users.api.views import RegistrationViewAV, LogoutViewAV, LoginViewAV
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# register ---> register acc
# login ---> login acc
# logout ---> logout acc
# token ---> issue token
# token/refresh ---> request for new token.

urlpatterns = [
    path('login/', LoginViewAV.as_view(), name='login'),
    path('register/', RegistrationViewAV.as_view(), name='register'),
    path('logout/', LogoutViewAV.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
    
]


