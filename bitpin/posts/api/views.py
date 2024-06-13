from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from bitpin.posts.api.serializers import CreatePostSerializer, ListPostSerializer, RatePostSerializer
from bitpin.posts.models import Post


class APICreatePostView(generics.CreateAPIView):
    """
    this view create new post
    input:
        title: str
        body: text
    """
    serializer_class = CreatePostSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return super().create(request, message='Create Post Successfully.', *args, **kwargs)


class ListPostView(generics.ListAPIView):
    """ show all post """
    serializer_class = ListPostSerializer
    permission_classes = [AllowAny]
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return super().list(request, message='Get all Post Successfully.', *args, **kwargs)


class RatePostView(generics.CreateAPIView):
    """
    create new rate to post
    input:
        post: int(post id)
        rate: int(0-5)

    """
    serializer_class = RatePostSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().create(request, message='Added Rate Successfully.', *args, **kwargs)


