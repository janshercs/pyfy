from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.portfolio_view.as_view(), name = 'portfolio'),
    path('portfolio/<int:pk>/delete',views.TradeDelete.as_view(), name = 'delete_trade'),
]