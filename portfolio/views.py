from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import DeleteView
from .models import Trade
from forms import add_trade
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class portfolio_view(LoginRequiredMixin,ListView):
    template_name = 'portfolio/portfolio.html'
    def get_queryset(self):
        #changing query set
        if self.request.user.is_authenticated:
            user = self.request.user
            return Trade.objects.filter(user = user)
        else: return Trade.objects.all()
        
    def get_context_data(self, **kwargs):
        #adding form into context passed into view
        context = super().get_context_data(**kwargs)
        context['form'] = add_trade()
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
