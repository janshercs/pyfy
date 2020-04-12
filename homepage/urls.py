from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name = 'homepage'),
    path('register/', views.register.as_view(), name = 'register' ),
    path('logout/', views.logout_view, name = 'logout'),
]