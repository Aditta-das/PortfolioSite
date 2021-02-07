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
	image = models.ImageField()
	# description
	description = models.TextField()
	# github link
	github = models.URLField(max_length=300, null=True, blank=True)
	# kaggle link
	kaggle = models.URLField(max_length=300, null=True, blank=True)
	# colab link
	colab = models.URLField(max_length=300, null=True, blank=True)
	# webapp
	webapp = models.URLField(max_length=300, null=True, blank=True)
	
	def __str__(self):
		return self.title

class IP(models.Model):
	ip_list = models.GenericIPAddressField(blank=True, null=True)

	def __str__(self):
		return self.ip_list


class CV(models.Model):
	file = models.FileField(upload_to="files")
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
	total_download = models.IntegerField(default=0, null=True, blank=True)
	unique_download = models.IntegerField(default=0, null=True, blank=True)
	ip = models.ManyToManyField(IP, blank=True)


	def __str__(self):
		return "CV"

class Contact(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	msg = models.TextField()

	def __str__(self):
		return self.name

class CommentAdd(models.Model):
	name = models.CharField(max_length=30)
	post_text = models.TextField()

	def __str__(self):
		return self.name
