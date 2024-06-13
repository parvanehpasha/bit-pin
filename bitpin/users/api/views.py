from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from .serializers import RegisterSerializer, LoginSerializer


class APIRegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return super().create(request, message='Login Successfully.', *args, **kwargs)


class LoginApiView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return super().create(request, message='Login Successfully.', *args, **kwargs)
