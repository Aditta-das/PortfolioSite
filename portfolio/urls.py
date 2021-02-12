from django.urls import path

from .views import *
from . import views
from django.conf.urls import url

urlpatterns = [
	path('', PortfolioView.as_view(), name="index"),
	path('error/', views.handler404, name="error")
]

handler404 = 'portfolio.views.handler404'