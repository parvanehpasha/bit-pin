from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from bitpin.abstract.models import AbstractModel
from .managers import UserManager


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    GENDER = [
        ("male", "Male"),
        ("female", "Female"),
    ]

    username = models.CharField(_('Username'), null=False, unique=True)
    mobile = models.CharField(_('Phone Number'), max_length=11, unique=True, null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    gender = models.CharField(max_length=6, choices=GENDER)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['mobile']
    objects = UserManager()

    class Meta:
        db_table = "user"
        verbose_name = _("user")
        ordering = ['-created_at']

    def __str__(self):
        return self.username
