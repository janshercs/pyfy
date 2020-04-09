from django.contrib import admin

# Register your models here.
from .models import Ticker,Trade

admin.site.register(Ticker)
admin.site.register(Trade)