from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	descp = HTMLField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	author = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()
	

	def __str__(self):
		return self.title