from django.urls import path
from blog.api.v1 import views





urlpatterns = [
    path('post/', 
         views.PostModelViewSet.as_view({'get':'list','post':'create'}), name='post-list'),  
    path('post/<int:pk>/',
          views.PostModelViewSet.as_view({'get':'retrieve',
                                     'put':'update',
                                     'patch':'partial_update',
                                     'delete':'destroy'}), name='post-detail'),  
                                
]

