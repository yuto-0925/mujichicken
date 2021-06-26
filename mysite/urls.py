"""mysite URL Configuration

[...]
"""
from django.contrib import admin
from django.urls import path

from insta import views

urlpatterns = [
    path('', views.templates, name='templates'),
    path('admin/', admin.site.urls),
]