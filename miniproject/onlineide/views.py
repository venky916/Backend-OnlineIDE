from django.http import HttpResponse
from .models import Submissions
from django.contrib.auth.models import User
from .serializers import UserSerializer,SubmissionSerializer
from .utils import create_code_file,execute_file
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.serializers import AuthTokenSerializer
# knox imports
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from multiprocessing import Process
# Create your views here.

def hello_world(request):
    return HttpResponse("Welcome to online ide")

class LoginView(KnoxLoginView):
    # login view extending KnoxLoginView
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        login(request,user)
        return super(LoginView, self).post(request, format=None)  


@api_view(http_method_names=['POST'])
@permission_classes((permissions.AllowAny,))
def register(request):
    serializer=UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user=serializer.save()
    return Response(UserSerializer(user).data,status=201)


class UserViewSet(ModelViewSet):
    serializer_class=UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset=User.objects.all()
    
    def list(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user).data,status=200)

    
class SubmissionViewSet(ModelViewSet):
    queryset=Submissions.objects.all()
    serializer_class=SubmissionSerializer
    permission_classes=(permissions.IsAuthenticated,)
    
    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        queryset=queryset.filter(user=request.user)
        return Response(self.get_serializer(queryset,many=True).data,status=200)
    
    def create(self, request, *args, **kwargs):
        request.data['status']="P"
        request.data['user']=request.user.pk
        file_name=create_code_file(request.data.get("code"),request.data.get("language"))
        
        serializer=SubmissionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        submission=serializer.save()
        
        p=Process(target=execute_file,args=(file_name,request.data.get("language"),submission.pk))
        p.start()
        
        # output=execute_file(file_name,request.data.get("language"))
        # request.data['output']=output
        # return super().create(request, *args, **kwargs)
        
        return Response(
            {
                "message":"Submitted succesfully"
            },status=200
        )
