from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager
# Create your models here.

class UserAccountManager(BaseUserManager):
    """ A custom user account manager """
    def create_user(self, email , name, password =None):
        if not email:
            raise  ValueError("User must have an email address")
        
        ## create the user 
        email = self.normalize_email(email)
        user = self.model(name = name, email = email)
        user.set_password(password)  ## a hashing fuction to hash the passsword before storing it in the db
        user.save()
        return user


    def create_superuser(self , email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class  UserAccount(AbstractBaseUser, PermissionsMixin):
    """ Class user account extneds build in user account with more features  """
    email = models.EmailField(max_length=264, unique=True) ## unique because we will use it in validating a unique user
    name = models.CharField(max_length=264)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager(); ## create a custom user account manager 

    ## by default django use username to authenticate users 
    # so we will override it 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['name']


    ## some getters 
    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return str(self.email)
