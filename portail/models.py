from django.db import models


class Dummy(models.Model):
    class Meta:
        abstract = True
