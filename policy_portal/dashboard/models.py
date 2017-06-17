from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from functools import partial
# Create your models here.

class phase_1(models.Model):

	team = models.ForeignKey(User,null=True,blank=True)
	#team = user.get_username
	
	def upload_path1(instance, filename):
		up1 = 'teams/%s/problem_images_upload/%s'%(instance.team, filename)
		print (up1)
		return up1
	
	def upload_path2(instance, filename):
		up2 = 'teams/%s/FIR_upload/%s'%(instance.team, filename)
		print (up2)
		return up2
	
	def upload_path3(instance, filename):
		up3 = 'teams/%s/news_articles_upload/%s'%(instance.team, filename)
		print (up3)
		return up3
	
	def upload_path4(instance, filename):
		up4 = 'teams/%s/miscellaneous_upload/%s'%(instance.team, filename)
		print (up4)
		return up4
				
	#location_image_upload = models.FileField(upload_to = 'location_image_uploads',blank=True,null=True)
	#location_image_upload = models.ImageField(upload_to = upload_path,blank=True,null=True)
	problem_images = models.IntegerField(help_text="Number of images of existing problems",blank=True,null=True)
	problem_images_upload = models.ImageField(upload_to = upload_path1,blank=True,null=True)
	FIR_number = models.IntegerField(help_text="Number of FIRs to be uploaded",blank=True,null=True)
	FIR_upload = models.FileField(upload_to = upload_path2,blank=True,null=True)
	news_articles_number = models.IntegerField(help_text="Number of News Articles",blank=True,null=True)
	news_articles_upload = models.FileField(upload_to = upload_path3,blank=True,null=True)
	miscellaneous_upload = models.FileField(upload_to = upload_path4, blank = True, null = True)
	miscellaneous_detail = models.CharField(max_length = 200, null = True, blank = True, help_text = 'Description of the miscellaneous file uploaded')
	
	#	user = models.OneToOneField(User,blank=True,null=True)

#class test_image(models.Model):
	
#	testing_upload = models.FileField(upload_to = 'test_folder', blank=True, null=True)