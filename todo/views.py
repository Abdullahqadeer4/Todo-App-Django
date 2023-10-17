from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from todo.models import Task
from todo.serializers import TodoSerializer

class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def list(self, request, *args, **kwargs):
        try:
            tasks = Task.objects.all()
            serializer = TodoSerializer(tasks, many=True)
            return Response(serializer.data)
        except Exception as e:
            # Handle exceptions gracefully
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        try:
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Handle exceptions gracefully
            return Response({'Error Fetching data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

