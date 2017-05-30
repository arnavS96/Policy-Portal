from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class Member(models.Model):
	member_name = models.CharField(max_length=50, help_text="Member's name")
	member_email = models.EmailField(max_length=50, help_text="Member's Email ID")
	member_contact=models.IntegerField(help_text="Member's Contact Number")
	# team= models.ForeignKey('Team', null=True)
	id_proof = models.ImageField(upload_to='ID_proofs')

	
	def __str__(self):
        
		return self.member_name

class Team(models.Model):
	    team_name = models.CharField(max_length=50, help_text="Enter your team name")
	    member_number = ((1,1),(2,2),(3,3),(4,4),(5,5))
	    total_members = models.IntegerField(choices=member_number, blank=False, default='1', help_text='Total Team Members')
	    city = models.CharField(max_length=200, help_text="City/Town")
	    state = models.CharField(max_length=200, help_text="State")
	    team_admin=models.ForeignKey(User,null=True,blank=True) 
	    
	    def __str__(self):
        
        	return self.team_name
# @receiver(post_save, sender=User)
# def create_user_team(sender, instance, created, **kwargs):
#     if created:
#         Team.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_team(sender, instance, **kwargs):
#     instance.team.save()

 

 


