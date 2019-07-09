from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class files(models.Model):
	note     = models.CharField(max_length=100)
	uploaded_at = models.DateTimeField(auto_now_add=True)
	document = models.FileField(upload_to='documents/%Y/%m/%d/')
	author = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)


	def __str__(self):
		return self.note
