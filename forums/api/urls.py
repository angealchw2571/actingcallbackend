from django.urls import path, include
#-------------------------------------------------------------
# rest_framework related.
#-------------------------------------------------------------
# This import is for Class based view.
from forums.api.views import PostsAV, PostsDetailAV, DiscussionAV ,DiscussionDetailAV
#-------------------------------------------------------------

# posts ----> thread
# discussion ---> comments inside the thread. 

urlpatterns = [
    path('posts/', PostsAV.as_view(), name='allposts'),
    path('posts/<int:pk>/', PostsDetailAV.as_view(), name='posts'),
    path('discussion/', DiscussionAV.as_view(), name='alldiscussion'),
    path('discussion/<int:pk>/', DiscussionDetailAV.as_view(), name='discussion')
   
]