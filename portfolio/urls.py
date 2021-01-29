from django.urls import path

from .views import *
from .import views

urlpatterns = [
	path('', PortfolioView.as_view(), name="index"),
]