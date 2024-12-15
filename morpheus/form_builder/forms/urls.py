from django.urls import path
from .views import form_create, form_success

urlpatterns = [
    path('create/', form_create, name='form_create'),
    path('success/', form_success, name='form_success'),
]
