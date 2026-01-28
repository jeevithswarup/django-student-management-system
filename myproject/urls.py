from django.contrib import admin
from django.urls import path, include  # include is important
from myapp.views import *
from vege.views import *
from api_work.views import *
from api_work.views2 import APILoginView


urlpatterns = [
    path("",login_page,name="home"),
    path("logout/",logout_page,name="logout_page"),
    path("receipe/",receipe,name="receipe"),
    path("register/",register,name="register"),
    path("zomato/",zomato_home,name="zomato_home"),
    path("data/",get_students,name="get_students"),
    path("results/<student_id>/", subject_mark, name="subject_mark"),
    path("students/",student_list),
    path("students/<int:pk>/",student_update),
    path("myportal/",student_portal),
    path("api/login/", APILoginView.as_view(), name="api_login"),
    path("admin/",admin.site.urls),
]
 
