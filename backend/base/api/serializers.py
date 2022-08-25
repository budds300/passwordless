from asyncio.windows_events import NULL
import email
from django.db import models
from django.core.validators import RegexValidator


from django.contrib.auth.models import (  BaseUserManager, AbstractBaseUser,PermissionsMixin)
# Create your models here.
class UserAccoutManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,phone_number,password=None):
            if not email:
                raise ValueError('Users must have an email address')
            email=self.normalize_email(email)
            email=email.lower( )
            if password is not None:
                user = self.model(
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        phone_number=phone_number,
                        password=password
                        
                    )
                user.save(using=self._db)
            else:
                user = self.model(
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        phone_number=phone_number,
                        password=password
                        
                    )
                user.set_unusable_password()
                user.save(using=self._db)
            return user


    def create_superuser(self,first_name,last_name,email,phone_number,password=None):
            """
            Creates and saves a superuser with the given email, date of
            birth and password.
            """
            user = self.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number,
                    password=password
                
                    
                )
            user.set_password(password)
            user.is_staff=True
            user.is_superuser=True
            user.is_admin = True
            user.save(using=self._db)
            return user
        
    
class UserAccount(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Please enter a valid phone number")
    phone_number=models.PositiveIntegerField (null=True)
    email=models.EmailField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects=UserAccoutManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name',"last_name",'phone_number']


def __str__(self):
    return self.email
    