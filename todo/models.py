from django.db import models
import uuid

class Base(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Task(Base):  
    TaskName = models.CharField(max_length=225)
    Description = models.TextField(max_length=500)
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey('self', on_delete=models.CASCADE, related_name="user_task")
