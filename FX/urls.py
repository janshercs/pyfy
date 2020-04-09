from django.urls import path
from . import views

app_name = 'FX'
urlpatterns = [
    path('', views.index.as_view( ), name = 'index'),
    path('spot/', views.FX.as_view(), name = 'spot'),
    path('chart/', views.chart.as_view(), name = 'chart')
]