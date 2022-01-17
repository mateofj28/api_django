from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):

    ''' manager for model userProfile '''

    # functions from terminal

    # create userProfile 
    def create_user(self, email, name, password=None):
        
        # don't have email
        if not email:
            raise ValueError('Email required')
        
        # regular email
        email = self.normalize_email(email)

        # create object userProfile
        user = self.model(email=email, name=name)

        # add pass
        user.set_password(password)

        # save user and pass has hachs (encrypted)
        user.save(using=self._db)

        return user

    # create admin (superUser)
    def create_superuser(self, email, name, password):

        # create user regular
        user = self.create_user(email, name, password)

        # declared super user
        user.is_superuser = True

        # theam?, yes
        user.is_staff = True

        # save super user
        user.save(using=self._db)

        return user



# django trae un modelo que podemos usar
# como sobre escritura, con ello podremos hacer login con el email

class UserProfile(AbstractBaseUser, PermissionsMixin):

    """ model user data base  """    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # if user is active for systememail, name, password
    is_active = models.BooleanField(default=True)
    # have a team ?
    is_staff = models.BooleanField(default=False)

    """ object manager """
    objects = UserProfileManager() # manager 

    # name login
    USERNAME_FIELD = 'email'
    # attribute required
    REQUIRED_FIELDS = ['name']

    #functions

    # required name
    def get_name(self):
        return self.name

    # representation user for admin
    def __str__(self):
        return self.email    