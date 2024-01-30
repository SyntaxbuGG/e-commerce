from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from base.models import TimeStampedModel

class Category(MPTTModel, TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    order = models.IntegerField(default=0)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        ordering = ['order']