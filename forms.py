from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from portfolio.models import Trade

class currency_pair_form(forms.Form):
    currency_choices = [('USD','USD'),('SGD','SGD'),('JPY','JPY'),('HKD','HKD')]
    base_choice = forms.CharField(label = 'base', widget=forms.Select(choices = currency_choices))
    pair_choice = forms.CharField(label = 'pair', widget=forms.Select(choices = currency_choices))

class registration_form(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class add_trade(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ['ticker', 'buy_price', 'volume']