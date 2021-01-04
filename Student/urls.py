from django.urls import path, include
from . import views


urlpatterns = [
    path('user/login/', views.loginPage, name="login"),
    path('Login/', views.Login, name="Login"),
    path('get/user/details/', views.get_user_details, name="get_user_details"),
    path('logout/user/', views.logout_user, name="logout"),
    
    path('admin/home/', views.admin_home, name="admin_home"),   
    path('add/course/', views.add_course, name="add_course"),
    path('add/course/save/', views.add_course_save, name="add_course_save"),
    path('add/student/', views.add_student.as_view(), name="add_student"),
    path('', views.PostListView.as_view(), name="student_list"),
    
]