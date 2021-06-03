from django.urls import path
from .views import cidadao, index, login

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('cidadao/', cidadao, name='cidadao'),
]