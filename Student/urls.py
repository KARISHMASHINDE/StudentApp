from django.urls import path, include
from . import views


urlpatterns = [
    path('user/login/', views.loginPage, name="login"),
    path('Login/', views.Login, name="Login"),
    path('get/user/details/', views.get_user_details, name="get_user_details"),
    path('logout/user/', views.logout_user, name="logout_user"),
    
    path('admin_home/', views.admin_home, name="admin_home"),
    
    path('student/profile/', views.student_profile, name="student_profile"),
    path('student/update/profile/', views.student_profile_update, name="student_profile_update"),
]