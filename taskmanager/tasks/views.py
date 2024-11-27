from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Task
from .serializers import TaskSerializer


class TaskPagination(PageNumberPagination):
    page_size = 5  # Customize page size
    page_size_query_param = 'page_size'

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = TaskPagination

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user)

        # Filtering by status
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)

        return queryset

    def perform_create(self, serializer):
        # Automatically associate the task with the authenticated user
        serializer.save(user=self.request.user)
