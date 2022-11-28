from django.db import models
from django.contrib.auth.models import AbstractBaseUser 
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

#User Profile Manger for Custom Model
class UserProfileManger(BaseUserManager):

    def create_user(self, email, name, password=None):
        """Create new user profile"""
        if not email:
            raise ValueError('User must have a email address')
        email = self.normalize_email(email) #email normalize from case sensitive
        user = self.model(email=email, name=name) #user profile created

        user.set_password(password)
        user.save(using=self._db)
        return user # Return newly created user

    def create_superuser(self, email, name, password):
        """Create and save new super user"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



# CUSTOM USER MODEL IN DJANGO WITH EMAIL AUTHENTICATION 
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user in system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #User Profile Manger
    objects = UserProfileManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
    
