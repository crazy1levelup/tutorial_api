from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models
from django.db import transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe

class Items(models.Model):
    type = models.CharField(null=True, max_length=20)
    number = models.IntegerField(unique=True, default=0)
    quantity = models.IntegerField(default=0)