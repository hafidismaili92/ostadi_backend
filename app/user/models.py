from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    """user manager"""
    def create_user(self,email,password=None,**extraFields):

        user = self.model(email=self.normalize_email(email),**extraFields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password=None,**extraFields):
        """create super user"""
        user = self.create_user(email=email,password=password,**extraFields)
        user.is_superuser=True
        user.is_staff = True
        user.is_default_student = False
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email= models.EmailField(max_length=200,unique=True)
    name= models.CharField(max_length=200)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    student_account = models.OneToOneField("profils.Student", on_delete=models.SET_NULL,null=True)
    professor_account = models.OneToOneField("profils.Professor", on_delete=models.SET_NULL,null=True)
    is_default_student = models.BooleanField(null=True)
    

    objects = UserManager()
    USERNAME_FIELD ="email"

    def is_student(self):
        return self.student_account is not None

    def is_professor(self):
        return self.professor_account is not None

