# https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
# https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
# from .manager import CustomUserManager
# from django.contrib.auth.base_user import AbstractBaseUser


# Custom User model
class User(AbstractUser):
	pass
"""
# Custom User model
class User(AbstractBaseUser):
	email = models.EmailField(max_length=255, unique=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'	# username is now an email field
	REQUIRED_FIELDS = [] # USERNAME_FIELD (email) and password are always required

	objects = CustomUserManager()

	def _str_(self):
		return self.email


# User Manager model
class CustomUserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('Email field is required')
		user = self.model(
			email=self.normalize_email(email)	# convert email domain to lowercase to avoid duplicates
		) 
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(email, password=password)
		user.is_staff = True
		user.is_admin = True
		user.is_active = True
		user.is_superuser = True
		user.save(using=self._db)
		return user
"""