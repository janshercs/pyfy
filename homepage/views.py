from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.generic import TemplateView
from forms import registration_form
from django.contrib.auth import login, logout, authenticate

# Create your views here.
class index(TemplateView):
    template_name = 'homepage/index.html'

class register(TemplateView):
    template_name = 'registration/register.html'
    def get(self, request):
        form = registration_form()
        context = {
            'form': form
        }
        return render(request, 'registration/register.html', context = context)

    def post(self,request):
        form = registration_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else: 
            form = registration_form(request.POST)
            return render(request, 'registration/register.html', {'form':form})

def logout_view(request):
    logout(request)
    return render(request,'registration/logout.html')

    
        
