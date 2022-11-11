from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import status
from knox.views import LoginView as BaseLoginView
from knox.auth import AuthToken
from .serializers import RegisterSerializer


# Create your views here.


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(BaseLoginView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = AuthToken.objects.create(user)[1]
        return Response({
            'token': token,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'bio': user.bio
            },
        })
