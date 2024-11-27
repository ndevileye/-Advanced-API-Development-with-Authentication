from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now, make_aware

# Task model definition
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Signal to schedule reminder email when a new task is created
@receiver(post_save, sender=Task)
def schedule_reminder(sender, instance, created, **kwargs):
    if created:
        # Import the task here to avoid circular import
        from .tasks import send_reminder_email

        # Ensure that the due_date is timezone-aware if it's not already
        due_date = instance.due_date
        if not due_date.tzinfo:
            due_date = make_aware(due_date)

        # Calculate the time difference between now and the task's due date
        time_difference = due_date - now()

        # If the due date is more than 24 hours away, schedule the reminder email
        if time_difference > timedelta(days=1):
            send_reminder_email.apply_async(
                args=[instance.id],
                eta=due_date - timedelta(days=1)  # Schedule the task 24 hours before due date
            )
