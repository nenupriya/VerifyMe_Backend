from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


GOOGLE_CLIENT_ID = 'your_client_id'
GOOGLE_CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'http://localhost:8000/api/auth/google/callback/'

# Create your models here.

class getUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request, format=None):
        userinfo = User.objects.get(username=request.user)
        serializer = UserSerializer(instance=userinfo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

