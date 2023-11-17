from django.shortcuts import render
from django.http  import HttpResponse,JsonResponse
import json
from .models import User,Todo
from .serializers import UserSerializer,TodoSerializer

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello /world you built an api")

def add(request):
    a=int(request.GET['a'])
    b=int(request.GET['b'])
    c=a+b
    response={
        "message":"Success",
        "sum":c
    }
    return JsonResponse(response,status=200)

def create_user(request):
    try:
        data=json.loads(request.body)
        
        # fields=["name","date_of_birth"]
        # for field in fields:
        #     if field not in data.keys():
        #         return JsonResponse({
        #             "message":field+" is mandatory"
        #         },status=400)
        # User.objects.create(name=data["name"],date_of_birth=data["date_of_birth"])
        # user=User.objects.get(name=data["name"])
        # print(data)
        # return JsonResponse({
        #     "name":user.name,
        #     "date_of_birth":user.date_of_birth,
        #     "id":user.id
        #     },
        #     status=201
        # )
        
        serializer=UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return JsonResponse(
            UserSerializer(user).data,status=200)
        

    except Exception as e:
        return JsonResponse({
            "error":e.__str__()
        },status=400)

def get_user(request):
    try:
        id=request.GET.get("id")
        user=User.objects.get(pk=id)
        
        # return JsonResponse({
        #     "name":user.name,
        #     "date_of_birth":user.date_of_birth,
        #     "id":user.id
        #     },
        #     status=201
        # )
        return JsonResponse(UserSerializer(user).data,status=201)
    except Exception as e:
        return JsonResponse({
            "error":e.__str__()
        },status=404)
        
        
def add_todo(request):
    try:
        data=json.loads(request.body)
        serializer=TodoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        todo=serializer.save()
        return JsonResponse(
            TodoSerializer(todo).data,status=201
        )
    except Exception as e:
        return JsonResponse({
            "error":e.__str__()
        },status=404)
        
def get_todo(request):
    try:
        id=int(request.GET.get("id"))
        todo=Todo.objects.get(pk=id)
        return JsonResponse(TodoSerializer(todo).data,status=200)
    
    except Exception as e:
        return JsonResponse(
            {
                "message":e.__str__()
            },status=404
        )