from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.task_data = {
            'title': 'Sample Task',
            'description': 'Task Description',
            'due_date': '2024-11-27T15:30:00Z',
            'status': 'pending',
        }

    def test_create_task(self):
        response = self.client.post('/api/tasks/', self.task_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tasks(self):
        Task.objects.create(user=self.user, **self.task_data)
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
