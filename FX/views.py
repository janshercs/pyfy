from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .utils import get_data, get_chart
from django.views.generic import TemplateView
from forms import currency_pair_form

class FX(TemplateView):
    template_name = 'FX/spot.html'
    
    '''def get_context_data(self,*args,**kwargs):
        request = request.POST
        context = {
            'spot':get_data(request['pair_choice'],request['base_choice'])
        }
        return context'''
    
    def get(self, request): 
        query = request.GET
        context = {
            'spot':get_data(query['pair_choice'],query['base_choice'])
        }
        return render(request, 'FX/spot.html', context = context)

class index(TemplateView): 
    template_name = 'FX/index.html'
    '''def get_context_data(self,*args,**kwargs):
        context = {
            'form': currency_pair_form()
        }
        return context'''
    def get(self, request):
        form = currency_pair_form()
        ctx = {'form': form}
        return render(request, 'FX/index.html', context = ctx)

class chart(TemplateView):
    template_name = 'FX/chart.html'
    def get(self, request):
        query = request.GET
        resp = get_chart(query['pair_choice'],query['base_choice'])
        context = {
            'plot_div': resp
        }
        return render(request, 'FX/chart.html', context = context)

    

    

# Create your views here.
