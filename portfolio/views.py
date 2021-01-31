from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from datetime import datetime
from weather import Scrap
from django.contrib import messages
# Fix the Bug CV Download

class PortfolioView(View):
	def get(self, request, *args, **kwargs):
		portfolio = Portfolio.objects.all()
		prods = Contact.objects.all()
		cv = CV.objects.get(pk=1) # CV Download Bug
		currenttime = int(datetime.now().strftime("%H"))
		print(currenttime)		
		area = (self.request.GET)
		area = "".join([v for k, v in area.items()])
		temp_cel = 0
		location = None
		day_type = None
		icon = None
		try:
			weather_api = Scrap(f"{area}").api_call()
			# print(day_type)
			if type(weather_api) != tuple:
				messages.info(self.request, 'Area Not found')
			else:
				temp_cel = weather_api[0] + temp_cel
				day_type = weather_api[1]
				wind_ = weather_api[2]
				humidity_ = weather_api[3]
				location = weather_api[4]
				country_ = weather_api[5]
				icon = weather_api[6]
				icon = f"/static/assets/weather/{icon}.png"
		except KeyError:
			pass
		return render(request, template_name="index.html", 
			context={"portfolio": portfolio, "currenttime": currenttime, "cv": cv, "temp_cel": temp_cel, "location": location, "day_type": day_type, "icon": icon})

	def post(self, request, *args, **kwargs):
		if self.request.method == "POST":
			name = self.request.POST["name"]
			email = self.request.POST["email"]
			phone = self.request.POST["phone"]
			msg = self.request.POST["msg"]
			prods = Contact(name=name, email=email, phone=phone, msg=msg)
			prods.save()
			return redirect("/")
		# return render(request, template_name="index.html")



