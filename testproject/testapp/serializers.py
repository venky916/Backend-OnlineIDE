from .models import User,Todo
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["name","date_of_birth"]

class TodoSerializer(serializers.ModelSerializer):
    # user=UserSerializer(read_only=True)
    class Meta:
        model=Todo
        fields="__all__"