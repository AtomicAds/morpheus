from django import forms
from .models import Form  # Assuming 'Form' is your model name

class FormModelForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'description', 'created_at']  # Include the fields you want to display

class CustomForm(forms.Form):
    # Add fields for a simple form
    name = forms.CharField(max_length=100, label='Form Name')
    description = forms.CharField(widget=forms.Textarea, label='Form Description')