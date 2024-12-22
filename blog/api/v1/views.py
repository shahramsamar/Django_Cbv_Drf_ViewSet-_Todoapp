from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from blog.api.v1.serializer import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status


class PostViewSet(viewsets.ViewSet):
    """Getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)

    def create(self, request):
        # Serialize the data from the request
        serializer = self.serializer_class(data=request.data)
        
        # Check if the data is valid
        if serializer.is_valid():
            # Save the new post to the database
            serializer.save()

            # Return a successful response with the created data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # If the data is invalid, return a bad request response with errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        post_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
