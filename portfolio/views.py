from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from .models import Portfolio
from datetime import datetime

class PortfolioView(View):
	def get(self, request, *args, **kwargs):
		portfolio = Portfolio.objects.all()
		currenttime = int(datetime.now().strftime("%H"))
		print(currenttime)
		if currenttime < 6 and currenttime > 0:
			print("night")
		else:
			print("day")
		return render(request, template_name="index.html", 
			context={"portfolio": portfolio, "currenttime": currenttime})