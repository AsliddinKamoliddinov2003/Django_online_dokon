from django.db import models
from django.db.models.fields import CharField
from django.utils import translation
from django.utils.translation import gettext as _

from parler.models import TranslatableModel, TranslatedFields


class Person(TranslatableModel):
    translation = TranslatedFields(
        address = models.CharField(max_length=255),
        available = models.CharField(max_length=255)
    )
    fullname = models.CharField(max_length=255, verbose_name=_("Fullname"))
    age = models.IntegerField(verbose_name=_("age"))

    def __str__(self):
        return self.address
        


