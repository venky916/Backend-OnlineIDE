from .models import User,Todo
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        
class TodoSerializer(serializers.ModelSerializer):
    user=UserSerializer() #SOMETHING WRONG HERE
    # user = serializers.RelatedField(source='User', read_only=True) #not display user
    user = serializers.PrimaryKeyRelatedField(read_only=False ,queryset=User.objects.all())
    class Meta:
        model=Todo
        fields="__all__"
        