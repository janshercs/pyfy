from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.generic import TemplateView
from . import macro_charts

# Create your views here.
class index(TemplateView):
    template_name = 'macro/index.html'
    def get(self, request):
        yield_spread = macro_charts.make_observation_chart('T10Y2Y', "10 Year 2 Year Yield Spread")
        context = {
            'plot_div': yield_spread
        }
        return render(request, 'macro/index.html', context = context)
