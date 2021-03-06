from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'FX'
urlpatterns = [
    path('', views.index.as_view( ), name = 'index'),
    path('spot/', views.FX.as_view(), name = 'spot'),
    path('chart/', views.chart.as_view(), name = 'chart')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)