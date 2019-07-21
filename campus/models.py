from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	descp = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	author = models.ForeignKey(User,on_delete=models.SET_NULL,db_column='author',to_field='username',blank=True,null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()
	

	def __str__(self):
		return self.title