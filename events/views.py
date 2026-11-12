from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from events.models import Event
from events.serializers import EventSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from events.permissions import IsOrganizerOrReadOnly
class EventListCreateView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsOrganizerOrReadOnly]
    def get(self,request):
        e=Event.objects.all()
        serializer_instance=EventSerializer(e,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer_instance=EventSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(organizer=request.user)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class EventRetrieveUpdateDelete(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsOrganizerOrReadOnly]
    def get(self,request,pk):
        e=get_object_or_404(Event,id=pk)
        serializer_instance=EventSerializer(e)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        e=get_object_or_404(Event,id=pk)
        self.check_object_permissions(request,e)
        serializer_instance=EventSerializer(instance=e,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(organizer=request.user)
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        e=get_object_or_404(Event,id=pk)
        self.check_object_permissions(request,e)
        e.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

