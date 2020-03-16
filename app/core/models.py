from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    """ Custom user Manger """ 

    def create_user(self, email, password=None, **etraFields):
        """ create new user and savesthe user""" 

        # Adding validation Checks to the email 
        if not email:
            raise ValueError("Users must have an emil address ")

        user = self.model(email=self.normalize_email(email), **etraFields)
        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_superuser(self, email, password):
        """Create super user """

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

# create the user model 

class user(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email as primary"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'