from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.endpoint_view, name='endpoint_view'),
]
