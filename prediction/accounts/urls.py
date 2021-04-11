from django.urls import path
from . import views
urlpatterns = [
    path('registration/' , views.register_uer,name="register"),
    path("login/", views.login_request, name="login"),
    path("home/", views.home, name="home"),
    path("doctor_info/", views.Doctor_info,name="doctor_info"),
    path('logout/',views.Logout,name="logout"),
    path("profile/",views.doctor_profile,name="profile"),
    path('doctor_page/',views.doctor_page,name="doctor_page"),
    path('testing',views.just_for_testing,name="just_for_testing")

]