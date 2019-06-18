from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models
from django.db import transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe

class Items(models.Model):
    name = models.CharField(null=True, max_length=20)
    type = models.CharField(null=True, max_length=20)
    videolink = models.CharField(null=True, max_length=20)
    description = models.TextField(blank=True, null=True)


class SavedItems(models.Model):
    nr = models.ForeignKey(Items,unique=True, default=None, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=20)
    type = models.CharField(null=True, max_length=20)
    videolink = models.CharField(null=True, max_length=20)
    description = models.TextField(blank=True, null=True)