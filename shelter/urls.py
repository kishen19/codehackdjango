from django.urls import path
from . import views

urlpatterns = [
    path('',views.handle_shel),
    path('entry',views.shel_entry),
]
