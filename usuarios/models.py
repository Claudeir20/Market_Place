from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None,  **extra_fields):
        if not email:
            raise ValueError("O email é Obrigatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=150)
    tipo = models.CharField(max_length=20, choices=[('cliente', 'Cliente'), ('vendedor', 'Vendedor'),  ('admin', 'Admin')], default='cliente')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    objects = UsuarioManager()

    def __str__(self):
        return self.email