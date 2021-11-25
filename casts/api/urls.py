from django.urls import path, include
#-------------------------------------------------------------
# rest_framework related.
#-------------------------------------------------------------
# This import is for Class based view.
from casts.api.views import CastCallAV, CastCallDetailAV
#-------------------------------------------------------------

# casts --> show all casting calls and add casting calls
# cast/:pk --> show individual casting calls, edit and delete.

urlpatterns = [
    path('', CastCallAV.as_view(), name='allcasts'),
    path('<int:pk>/', CastCallDetailAV.as_view(), name='allcasts-detail')

]
