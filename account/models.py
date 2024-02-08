from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.create_activation_code()
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    STATUS_CHOICES = (
        ('user', 'Пользователь'),
        ('seller', 'Продавец')
    )
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    is_seller = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='user')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code
    
    def __str__(self):
        return self.email

    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')


