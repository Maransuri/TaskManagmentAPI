from rest_framework import generics, permissions, pagination, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.http import Http404
from .models import Task
from .serializers import TaskSerializer
from .filters import TaskFilter  
from .permissions import IsAdminOrOwner  

class TaskPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    pagination_class = TaskPagination

    def get_queryset(self):
        if self.request.user.is_staff:
             return Task.objects.all().select_related('user').order_by('-created_at')  # Ensure ordering
        return Task.objects.filter(user=self.request.user).select_related('user').order_by('-created_at')  # Ensure ordering
    def delete(self, request, *args, **kwargs):
        task = self.get_object()
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_200_OK)


    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Task.objects.all().select_related('user')
        return Task.objects.filter(user=self.request.user).select_related('user')

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)
