from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forms/', include('forms.urls')),  # Include form URLs
]