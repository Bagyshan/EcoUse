from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, Group, Permission

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        if not email:
            return ValueError('Почта должна обязательно передаваться!')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.create_activation_code()
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        return self._create_user(email, password, **kwargs)

class CustomUser(AbstractUser):
    STATUS_CHOICES = (
        ('user', 'Пользователь'),
        ('Seller', 'Продавец')
    )
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)  
    activation_code = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=100)
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