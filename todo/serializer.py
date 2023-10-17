from rest_framework import serializers
from todo.models import task
class TodoSerializer(serializers.ModelSerializer):
    
    class meta:
        model = task
        exclude = ['updated_at']