from celery import shared_task
from django.core.mail import send_mail
from .models import Task

@shared_task
def send_reminder_email(task_id):
    try:
        task = Task.objects.get(id=task_id)
        send_mail(
            'Task Reminder',
            f'Reminder: Your task "{task.title}" is due in 24 hours.',
            'no-reply@example.com',  # Update to your "from" email
            [task.user.email],
            fail_silently=False,
        )
    except Task.DoesNotExist:
        print(f"Task with id {task_id} does not exist.")
