from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
# router.register("user",views.CustomerViewSet)
router.register("prescription",views.PrescriptionViewSet)

urlpatterns=[
    path("",views.health,name="health"),
    path("register",views.register,name="register"),
    path("login",views.LoginView.as_view(),name="login"),
    path("test",views.test,name="test"),
]

urlpatterns+=router.urls