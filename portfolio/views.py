from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.generic import TemplateView, ListView
from . import models


# Create your views here.
class portfolio_view(ListView):
    model = models.Trade
