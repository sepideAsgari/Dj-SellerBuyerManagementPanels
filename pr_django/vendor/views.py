from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializers import UserSerializer, VendorInfo

# User = get_user_model()


# class VendorRegisterView(APIView):
#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = VendorInfo(users, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
