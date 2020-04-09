from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ticker(models.Model):
    ticker = models.CharField(max_length = 100)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Trade(models.Model):
    buy_price = models.DecimalField(max_digits = 10, decimal_places=3)
    volume = models.PositiveIntegerField()
    ticker = models.ForeignKey('Ticker', on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE,)

    def __str__(self):
        return "Trade number: {}".format(self.id)