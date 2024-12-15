# forms/models.py
from django.db import models

class Form(models.Model):
    title = models.CharField(max_length=200)

class Field(models.Model):
    form = models.ForeignKey(Form, related_name="fields", on_delete=models.CASCADE)
    field_type = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    required = models.BooleanField(default=False)
    options = models.JSONField(null=True, blank=True)  # For fields like dropdown or radio buttons