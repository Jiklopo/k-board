from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class UserFaculty(models.TextChoices):
    FIT = ('fit', 'Faculty Of Information Technologies')
    FGGE = ('fgge', 'Faculty of Geology and Geological Exploration')
    BS = ('bs', 'Business School')
    ISE = ('ise', 'International School of Economics')
    KMA = ('kma', 'Kazakh Maritime Academy')
    SMC = ('smc', 'School of Mathematics and Cybernetics')
    SCE = ('sce', 'School of Chemical Engineering')


class UserInfo(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
    admission_year = models.IntegerField(
        validators=[MinValueValidator(2001), MaxValueValidator(datetime.date.today().year)],
        blank=True, null=True)
    telegram_username = models.CharField(max_length=32)
    faculty = models.CharField(max_length=4, choices=UserFaculty.choices, blank=True, null=True)


class AddCategories(models.IntegerChoices):
    LOST = 10
    FOUND = 11


class Add(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250, blank=True)
    created = models.DateTimeField(auto_created=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.IntegerField(AddCategories.choices)
