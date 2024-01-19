from django.db import models
from django import forms
from django.core import validators
# Create your models here.

def check_for_a(value):
    if value.lower()[0]=='a':
        raise forms.ValidationError('invalid')

class Student(models.Model):
    Sname=models.CharField(max_length=100,primary_key=True,validators=[check_for_a])
    Sage=models.IntegerField()
    Smobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    def __str__(self):
        return self.Sname