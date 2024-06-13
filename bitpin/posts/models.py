from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import CheckConstraint, Q
from django.utils.translation import gettext_lazy as _
from bitpin.abstract.models import AbstractModel
from bitpin.users.models import User


class Post(AbstractModel):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, related_name='user')
    title = models.CharField(_('Title'), max_length=256, null=False)
    body = models.TextField(_('Caption'), null=False)
    rate_ave = models.IntegerField('Rate Average', default=0, null=True)

    class Meta:
        db_table = "post"
        verbose_name = _("post")
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class RatePost(AbstractModel):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, related_name='user_rate')
    post = models.ForeignKey(Post, verbose_name=_('post'), on_delete=models.CASCADE, related_name='post_rate')
    rate = models.IntegerField(_('Rate'), validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)

    class Meta:
        db_table = "Rate_post"
        verbose_name = _("Rate_post")
        constraints = (
            CheckConstraint(
                check=Q(rate__gte=0) & Q(rate__lte=5),
                name='rate'),
        )

    def __str__(self):
        return self.post.__str__
