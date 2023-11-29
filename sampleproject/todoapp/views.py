# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import User,Todo
from .serializers import UserSerializer,TodoSerializer


# Create your views here.
def hello(request):
    return JsonResponse({
        "message":"Hello Welcome to Todoapp"
    },status=200)
    
# @api_view(http_method_names=["post"])
# def create_user(request):
#     # print(request.query_params['id'])
#     print(request.data)
#     return Response({
#         "meaasage":"Received"
#     },status=201)


class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
class Todo(ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    