from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('Please Provide Email Address')    
        normalizemail=self.normalize_email(email)
        UPO=self.model(email=normalizemail,first_name=first_name,last_name=last_name)
        UPO.set_password(password)
        UPO.save()
        return UPO
    def create_superuser(self,email,first_name,last_name,password):
        UPO=self.create_user(email,first_name,last_name,password)
        UPO.is_staff=True
        UPO.is_superuser=True
        UPO.save()
        return UPO

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(primary_key=True,max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']
    
    def __str__(self):
        return self.first_name+" "+self.last_name         #By default it will show email