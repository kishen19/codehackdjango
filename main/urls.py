from django.urls import path
from . import views

urlpatterns = [
    path('',views.handle),
    path('update', views.index),
    path('submit', views.submit),
    path('entry',views.entry),
    path('supply',views.supplyindex),
    path('supplied',views.supply),
]
