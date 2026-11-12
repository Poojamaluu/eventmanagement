from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        self.request.user.auth_token.delete()

        return Response({"message": "Logout Successfull"})
