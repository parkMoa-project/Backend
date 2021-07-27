from django.urls import path
from django.contrib import admin
from django.urls import path
from rest_framework.schemas.inspectors import ViewInspector
from app import views

from . import views

urlpatterns = [
    path('', views.SearchView.as_view()),
]
