from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.


class AccountManager(BaseUserManager):
    """Manager for account"""

    def create_user(self, first_name, last_name, email, password=None):
        """Create a new account"""

        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(first_name=first_name,
                          last_name=last_name, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password):
        """Create and save a new superuser with given deatils"""

        user = self.create_user(first_name, last_name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    """Database model for accouonts in the system"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(
        max_length=255, unique=True, blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    def get_full_name(self):
        """Retrieve full name of account"""
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        """Retrieve short name of account"""
        return f'{self.first_name}'

    def __str__(self):
        """Return string representation of our account"""
        return self.get_full_name()



