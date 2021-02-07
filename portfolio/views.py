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
		links = []
		prods = Contact.objects.all()
		cv = get_object_or_404(CV, pk=1) # CV Download Bug
		currenttime = int(datetime.now().strftime("%H"))
		ip = IP()
		client_ip = request.META['REMOTE_ADDR']
		if client_ip not in str():
			pass
		area = self.request.GET
		area = "".join([v for k, v in area.items()])
		print(type(area))
		temp_cel = 0
		location = None
		day_type = None
		icon = None
		try:
			if area:
				weather_api = Scrap(f"{area}").api_call()
			else:
				weather_api = Scrap(f"bangladesh").api_call()
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
		comments = CommentAdd.objects.all()
		return render(request, template_name="index.html", 
			context={"portfolio": portfolio, "currenttime": currenttime, "cv": cv, "temp_cel": temp_cel, "location": location, "day_type": day_type, "icon": icon, "comments": comments})

	def post(self, request, *args, **kwargs):
		if self.request.method == "POST" and 'btnform1' in self.request.POST:
			name = self.request.POST["name"]
			email = self.request.POST["email"]
			phone = self.request.POST["phone"]
			msg = self.request.POST["msg"]
			prods = Contact(name=name, email=email, phone=phone, msg=msg)
			print(prods)
			prods.save()
			return redirect("/")

		elif self.request.method == "POST" and "btnform2" in self.request.POST:
			name = self.request.POST["name"]
			post_text = self.request.POST["post_text"]
			cmnts = CommentAdd(name=name, post_text=post_text)
			cmnts.save()
			return redirect("/")



