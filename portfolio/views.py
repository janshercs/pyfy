from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.forms import inlineformset_factory
from .models import Trade, Ticker
from forms import add_trade
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Min, Sum


# Create your views here.
class portfolio_view(LoginRequiredMixin,ListView):
    template_name = 'portfolio/portfolio.html'
    
    def get_queryset(self):
        #changing query set
        if self.request.user.is_authenticated:
            user = self.request.user
            trades = Trade.objects.filter(user = user)
            
            return trades
        else: return Trade.objects.all()
        
    def get_context_data(self, **kwargs):
        #adding form into context passed into view
        context = super().get_context_data(**kwargs)
        context['form'] = add_trade()
        context['total'] = sum(lt.cost for lt in context['trade_list'])
        return context

    def post(self, request):
        form = add_trade(request.POST)
        if form.is_valid():
            form_object = form.save(commit = False)
            form_object.user = self.request.user
            form.save()
        return redirect(reverse('portfolio:portfolio'))

class TradeDelete(DeleteView):
    template_name = 'portfolio/delete.html'
    model = Trade
    success_url = reverse_lazy('portfolio:portfolio')

class TradeUpdate(UpdateView):
     template_name = 'portfolio/update.html'
     model = Trade
     fields = ['ticker','buy_price', 'volume','date']
     success_url = reverse_lazy('portfolio:portfolio')
