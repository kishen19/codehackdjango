from django.urls import path
from . import views

urlpatterns = [
    path('',views.handle),
    path('getpoints',views.get_points),
]
