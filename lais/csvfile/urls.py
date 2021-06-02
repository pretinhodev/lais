from django.urls import path
from .views import local_upload

urlpatterns = [
    path('local_upload/', local_upload),
]