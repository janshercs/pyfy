from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.generic import TemplateView, CreateView
from django.urls import reverse, reverse_lazy
from forms import finplanner
# Create your views here.

class planner(TemplateView):
    template_name = 'finplanner/planner.html'

    def get(self, request):
        form = finplanner()
        return render(request, 'finplanner/planner.html' ,{'form':form})