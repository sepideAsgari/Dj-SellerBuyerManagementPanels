from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, VendorInfo


# User = get_user_model()

class UserInfoView(APIView):
    def get(self, request, format=None):
        user = request.user
        if user.is_authenticated:
            serializer = UserSerializer(user)
            print(serializer)
            return Response(serializer.data)
        else:
            return Response({'error': 'User is not authenticated or is admin'}, status=status.HTTP_401_UNAUTHORIZED)


class VendorRegisterView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = VendorInfo(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VendorInfo(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserInfoView(APIView):
#     def get(self, request):
#         if request.user.is_authenticated:
#             user = request.user
#             serializer = UserSerializer(user)
#             return Response(serializer.data)
#         else:
#             return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
# @api_view(['GET'])
# class UserInfoView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         user = request.user
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
