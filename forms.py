from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from portfolio.models import Trade, Ticker
from macro.models import Blogpost

class currency_pair_form(forms.Form):
    currency_choices = [('USD','USD'),('SGD','SGD'),('JPY','JPY'),('HKD','HKD')]
    base_choice = forms.CharField(label = 'base', widget=forms.Select(choices = currency_choices))
    pair_choice = forms.CharField(label = 'pair', widget=forms.Select(choices = currency_choices))

class registration_form(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DateInput(forms.DateInput):
    input_type = 'date'


class add_trade(forms.ModelForm):
    
    class Meta:
        model = Trade
        fields = ['ticker','buy_price', 'volume','date']
        widgets = {
            'date': DateInput
        }

    new_ticker = forms.CharField(max_length=30, required = False)
    new_ticker_name = forms.CharField(max_length=30, required = False)

    def __init__(self,*args, **kwargs):
        super(add_trade, self).__init__(*args, **kwargs)
        self.fields['ticker'].required = False
    
    def clean(self):
        ticker = self.cleaned_data.get('ticker')
        new_ticker = self.cleaned_data.get('new_ticker')
        new_ticker_name = self.cleaned_data.get('new_ticker_name')
        if not ticker and not new_ticker:
            raise forms.ValidationError('Must specify either ticker or new ticker')
        elif not ticker:
            if not new_ticker_name:
                raise froms.ValidationError('Must specify ticker name')
            else:
                ticker, created = Ticker.objects.get_or_create(ticker = new_ticker,name = new_ticker_name)
                self.cleaned_data['ticker'] = ticker

class finplanner(forms.Form):
    c_age = forms.IntegerField(label = 'Current age')
    r_age = forms.IntegerField(label = 'Target retirement age')
    salary = forms.IntegerField(label = 'Current monthly salary')
    expense = forms.IntegerField(label = 'Current monthly expenses')
    time_remaining = forms.IntegerField(label = 'Time horizon left')
    savings = forms.IntegerField(label = 'Current monthly savings')
    interest = forms.IntegerField(label = 'Risk Free Interest rates')
    inflation = forms.IntegerField(label = 'Inflation rate (%)', 
    #help_text='Average long term inflation rate is about 2%, though it has been about <1% recently'
    )
    returns = forms.IntegerField(label = 'Annual Returns (%)')
    r_expense = forms.FloatField(label = 'Retirement expense')
    final_savings = forms.IntegerField(label = 'Accumulated wealth before retiring')
    final_years = forms.IntegerField(label = 'Years left after retirement with expected life span of 80')
    





# https://stackoverflow.com/questions/8996451/save-new-foreign-key-with-django-form

# class add_ticker(forms.ModelForm):
#     class Meta:
#         model = Ticker
#         fields = ['ticker', 'name']