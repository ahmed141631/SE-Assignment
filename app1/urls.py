from django.urls import path
from . import views

urlpatterns = [
   path("home/",views.HomePage,name="home"),
   path("",views.Signup,name="signup"),
   path("login/",views.Login,name="login"),
   path('logout/',views.LogoutPage,name='logout'),
    

]