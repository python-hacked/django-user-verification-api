from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,Group, Permission
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('Users must have an Email Address')
        email = self.normalize_email(email)
        user = self.model(email=email, is_active = False)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,email,password = None):
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    # Add related_name arguments for groups and user_permissions fields
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

class OTP(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.email} - {self.otp_code}"
    
