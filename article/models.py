from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=20)
	
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    publ_date = models.DateTimeField('Publication Date')
    category = models.ForeignKey(Category)
    hero_image = models.ImageField(upload_to='hero-images/')
    optional_image = models.ImageField(upload_to='opt-images/')
    body_text = models.TextField()

    def was_published_recently(self):
        return self.publ_date > timezone.now() - datetime.timedelta(days=1)

