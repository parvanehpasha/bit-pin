from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractModel(models.Model):
    created_at = models.DateTimeField(_("Create"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Update"), auto_now=True)

    class Meta:
        abstract = True
