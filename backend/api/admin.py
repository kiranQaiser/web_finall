# api/admin.py
from django.contrib import admin
from .models import Book  # Make sure you import the correct model

admin.site.register(Book)
