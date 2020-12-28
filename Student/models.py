Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@KARISHMASHINDE 
vijaythapa333
/
django-student-management-system
2
3433
Code
Issues
Pull requests
Actions
Projects
1
Wiki
Security
Insights
django-student-management-system/student_management_app/models.py /
@vijaythapa333
vijaythapa333 Add Result on Staff Panel Complete
Latest commit 15058f2 on Jul 7
 History
 1 contributor
199 lines (150 sloc)  7.19 KB
  
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type = ((1, "Admin"), (2, "Student"))
    user_type = models.CharField(default=1, choices=user_type, max_length=10)



