from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.serializers import PostSerializer
from post.models import Post


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().select_related('author').prefetch_related('category')


