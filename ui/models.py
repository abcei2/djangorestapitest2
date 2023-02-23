from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager

"""  
    Custom user model manager where email is the unique identifiers  
    for authentication instead of usernames.  
    """


class CustomUserManager(BaseUserManager):
    """  
    Custom user model manager where email is the unique identifiers  
    for authentication instead of usernames.  
    """

    def create_user(self, email, password, **extra_fields):
        """  
        Create and save a User with the given email and password.  
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """  
        Create and save a SuperUser with the given email and password.  
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

    def get_full_name(self):
        '''  
        Returns the first_name plus the last_name, with a space in between.  
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''  
        Returns the short name for the user.  
        '''
        return self.first_name


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField('email_address', unique=True, max_length=200)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    login = models.CharField(primary_key=True, max_length=255)

    pswd = models.CharField(max_length=255)
    name = models.CharField(max_length=64, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    activation_code = models.CharField(max_length=32, blank=True, null=True)
    priv_admin = models.CharField(max_length=1, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
