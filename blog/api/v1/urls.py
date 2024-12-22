from django.urls import path
from blog.api.v1 import views

app_name = 'api-v1'  


urlpatterns = [
    path('post/', 
         views.PostViewSet.as_view({'get':'list','post':'create'}), name='post-list'),  
    path('post/<int:pk>/',
          views.PostViewSet.as_view({'get':'retrieve',
                                     'put':'update',
                                     'patch':'partial_update',
                                     'delete':'destroy'}), name='post-detail'),  
                                
]

