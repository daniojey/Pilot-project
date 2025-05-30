from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)

    def __str__(self):
        return  self.username

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class UsersGroup(models.Model):
    name = models.CharField(verbose_name="Назва группи", max_length=100,unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'users_group'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class UsersGroupMembership(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE , related_name='Учистник')
    group = models.ForeignKey(UsersGroup, on_delete=models.CASCADE, related_name='Участники')
    owner = models.BooleanField(default=False, verbose_name="Учитель группи")

    def __str__(self):
        return f"{self.user} - {self.group}"

    class Meta:
        db_table = 'user_group_membership'
        verbose_name = 'Членство пользователя в группе'
        verbose_name_plural = 'Членства пользователей в группах'


class LoginAttempt(models.Model):
    email = models.EmailField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.email or self.id_address} at {self.timestamp} - {'Sucess' if self.success else 'Filed'}"
    

    class Meta:
        db_table = 'loginattempt'
        verbose_name = 'Попытки логина'
        verbose_name_plural = 'Попытки логинов'
