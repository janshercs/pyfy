from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.generic import TemplateView, CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import macro_charts
from .models import Blogpost

# Create your views here.
class index(TemplateView):
    template_name = 'macro/index.html'
    def get(self, request):
        yield_spread = macro_charts.make_observation_chart('T10Y2Y', "10 Year 2 Year Yield Spread")
        context = {
            'plot_div': yield_spread
        }
        return render(request, 'macro/index.html', context = context)

class blog(TemplateView):
    template_name = 'macro/blog.html'
    def get(self, request):
        #pull 5x posts out in order of latest date, and render
        posts = Blogpost.objects.order_by('-pub_date')[:5]
        context = {
            'posts' : posts
        }

        return render(request, 'macro/blog.html', context = context)

class makepost(LoginRequiredMixin,CreateView):
    template_name = 'macro/makepost.html'
    model = Blogpost
    fields = ['title', 'content']
    
    def form_valid(self, form): #hijacks the form validation process and adds the user in automatically
        form_object = form.save(commit = False)
        form_object.author = self.request.user
        form.save()
        return redirect(reverse('macro:blog'))


    
