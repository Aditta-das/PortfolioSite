from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
import random, string
from django.conf import settings
# Create your models here.

class Portfolio(models.Model):
	# title
	title = models.CharField(max_length=100)
	# image
	image = models.ImageField(upload_to="static/profile/")
	# description
	description = models.TextField()
	# github link
	github = models.URLField(max_length=300, null=True, blank=True)
	# kaggle link
	kaggle = models.URLField(max_length=300, null=True, blank=True)
	# colab link
	colab = models.URLField(max_length=300, null=True, blank=True)
	
	def __str__(self):
		return self.title
