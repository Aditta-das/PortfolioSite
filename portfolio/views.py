from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from datetime import datetime


# Fix the Bug CV Download

class PortfolioView(View):
	def get(self, request, *args, **kwargs):
		portfolio = Portfolio.objects.all()
		prods = Contact.objects.all()
		cv = CV.objects.get(pk=1) # CV Download Bug
		currenttime = int(datetime.now().strftime("%H"))
		print(currenttime)
		return render(request, template_name="index.html", 
			context={"portfolio": portfolio, "currenttime": currenttime, "cv": cv})

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



