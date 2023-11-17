from django.urls import path
from .views import *

urlpatterns=[
    path("",hello_world,name="hello"),
    path("add",add,name="add"),
    path("add_user",create_user,name="add_user"),
    path('get_user',get_user,name="get_user"),
    path("add_todo",add_todo,name="add_todo"),
    path("get_todo",get_todo,name="get_todo"),
]