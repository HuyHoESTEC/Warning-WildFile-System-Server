from django.urls import path
from . import views

urlpatterns = [
    path('wildfire/', views.wildfire_view),
]
