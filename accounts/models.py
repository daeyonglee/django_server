from django.core.mail import send_mail
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website_url = models.URLField(blank=True)


def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)

    # send_mail(
    #     '환영합니다',
    #     'Here is the message.',
    #     'me@ldy.com',
    #     [user.email],
    #     fail_silently=False,
    # )


post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)
