from asyncio.windows_events import NULL
import email
from django.db import models
from django.core.validators import RegexValidator


from django.contrib.auth.models import (  BaseUserManager, AbstractBaseUser,PermissionsMixin)
# Create your models here.
class UserAccoutManager(BaseUserManager):
    
      def create_user(self, username, email, phone_number,password,**other_fields):
            if not email:
                raise ValueError('Email address is required!')
            email = self.normalize_email(email)
            if password is not None:
                user = self.model(username=username,email=email, phone_number=phone_number,password=password, **other_fields)
                user.save()
            else:
                user = self.model(username=username,email=email, phone_number=phone_number, password=password,**other_fields)
                user.set_unusable_password()
                user.save()

            return user

      def create_superuser(self,username, email, phone_number,password, **other_fields):
            other_fields.setdefault('is_staff', True)
            other_fields.setdefault('is_superuser', True)
            other_fields.setdefault('is_active', True)
      
            if other_fields.get('is_staff') is not True:
                raise ValueError('Superuser must be assigned to is_staff=True')
        
            if other_fields.get('is_superuser') is not True:
                raise ValueError('Superuser must be assigned to is_superuser=True')
            user =  self.create_user(username,email, phone_number, password, **other_fields)
            user.set_password(password)
            user.save()
            return user

  
class UserAccount(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Please enter a valid phone number")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
   
    objects = UserAccoutManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    def __str__(self):
        return self.email
    