# forms/serializers.py
from rest_framework import serializers
from .models import Form, Field

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['id', 'label', 'field_type', 'required', 'options']

class FormSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)

    class Meta:
        model = Form
        fields = ['id', 'title', 'fields']
