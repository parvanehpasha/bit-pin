from django.db.models import Subquery, Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from bitpin.posts.models import RatePost


@receiver(post_save, sender=RatePost)
def log_otp_creation(sender, instance, **kwargs):
    """ this calculates rate average for post """
    post = instance.post
    post_rate = post.post_rate.order_by('user_id', 'created_at').distinct(
        'user_id')
    rate_ave = post.post_rate.filter(id__in=Subquery(post_rate.values('id'))).aggregate(Avg('rate'))['rate__avg'] or 0.0
    if post is not None:
        post.rate_ave = rate_ave
        post.save()
