# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from .signals import test_signal
# Create your models here.
from django.db.models.signals import post_save


class TimeStampedModel(models.Model):
    date_last_modified = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(_('phonenumber'),null=True,blank=True)

    def __str__(self):
        return u'Person {}{}'.format(self.user.first_name,self.user.last_name)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        ordering = ['user__first_name']
        unique_together =['user','phone_number']

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

post_save.connect(create_user_profile,sender=User)
post_save.connect(save_user_profile,sender=User)