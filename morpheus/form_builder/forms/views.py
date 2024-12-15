from rest_framework import viewsets
from .models import Form, Field
from .serializers import FormSerializer

class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

from django.shortcuts import render

def index(request):
    return render(request, 'forms/index.html')

# forms/views.py
from django.shortcuts import redirect

def index(request):
    return redirect('/api/')

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to the Form Builder Application</h1>")

from django.shortcuts import render

def form_create(request):
    return render(request, 'template_name.html')

from .views import form_create, form_success
