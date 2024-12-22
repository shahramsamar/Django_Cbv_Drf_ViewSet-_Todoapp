
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from blog.api.v1.serializer import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import mixins


# class PostList(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
#     """ getting a list of post and creating new posts"""
#     permission_classes =[IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
    
#     def get(self, request, *args, **kwargs):
#         """
#         Retrieve a list of posts.

#         This method handles GET requests to retrieve a list of all active posts.
#         It uses the ListModelMixin to process the request and return a list of
#         Post objects.

#         Args:
#             request (Request): The HTTP request object.
#             *args: Variable length argument list.
#             **kwargs: Arbitrary keyword arguments.

#         Returns:
#             Response: The HTTP response containing the list of posts.
#         """
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         """
#         Create a new post with the provided data.

#         This method handles POST requests to create a new post. It uses the
#         CreateModelMixin to process the request and create a new Post object.

#         Args:
#             request (Request): The HTTP request object.
#             *args: Variable length argument list.
#             **kwargs: Arbitrary keyword arguments.

#         Returns:
#             Response: The HTTP response containing the newly created post data.
#         """
#         return self.create(request, *args, **kwargs)

class PostList(ListCreateAPIView):
    """ getting a list of post and creating new posts"""
    permission_classes =[IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

class PostDetail(RetrieveUpdateDestroyAPIView):
    """ getting detail of the post and edit plus removing it"""
    permission_classes =[IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
   
# class PostDetail(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     """ getting detail of the post and edit plus removing it"""
#     permission_classes =[IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
#     # lookup_field = "id" change the url when i have id 

#     def get(self, request, *args, **kwargs):
#         """
#         Retrieve details of a specific post.

#         This method handles GET requests to retrieve the details of a single post.
#         It uses the RetrieveModelMixin to process the request and return the
#         details of a specific Post object.

#         Args:
#             request (Request): The HTTP request object.
#             *args: Variable length argument list.
#             **kwargs: Arbitrary keyword arguments.

#         Returns:
#             Response: The HTTP response containing the details of the requested post.
#         """
#         return self.retrieve(request, *args, **kwargs)
     
#     def put(self, request, *args, **kwargs):
#         """
#         Update an existing post with the provided data.

#         This method handles PUT requests to update an existing post. It uses the
#         UpdateModelMixin to process the request and update the Post object.

#         Args:
#             request (Request): The HTTP request object containing the updated data.
#             *args: Variable length argument list.
#             **kwargs: Arbitrary keyword arguments.

#         Returns:
#             Response: The HTTP response containing the updated post data.
#         """
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         """
#         Delete a specific post.

#         This method handles DELETE requests to remove a specific post. It uses the
#         DestroyModelMixin to process the request and delete the Post object.

#         Args:
#             request (Request): The HTTP request object.
#             *args: Variable length argument list.
#             **kwargs: Arbitrary keyword arguments.

#         Returns:
#             Response: The HTTP response indicating the success of the deletion.
#         """
#         return self.destroy(request, *args, **kwargs)