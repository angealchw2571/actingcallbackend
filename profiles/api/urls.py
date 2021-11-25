from django.urls import path, include
#-------------------------------------------------------------
# rest_framework related.
#-------------------------------------------------------------
# This import is for Class based view.
from profiles.api.views import ProfilesAV, ProfilesDetailAV
#-------------------------------------------------------------

# profiles --> show all active user profiles and add profile details
# profiles/:username --> show profile of individual user, edit and delete.

urlpatterns = [
    path('', ProfilesAV.as_view(), name='profiles'),
    path('<str:username>/', ProfilesDetailAV.as_view(), name='profiles-details')
   
]