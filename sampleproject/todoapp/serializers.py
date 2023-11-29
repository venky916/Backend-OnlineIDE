from .models import User,Todo
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        
class TodoSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Todo
        fields="__all__"