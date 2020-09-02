from django.urls import path
from . import views

app_name = "macro"
urlpatterns = [
    #path('', views.index.as_view(), name = 'macro-index'),
    path('', views.blog.as_view(), name = 'blog'),
    path('create/', views.makepost.as_view(), name = 'create'),
]