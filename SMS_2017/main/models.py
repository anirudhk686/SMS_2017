from __future__ import unicode_literals
from django.db import models


start_money=1000000 #<complete> decide

class Team(models.Model):
	team_no = models.CharField(primary_key=True, max_length=3) #For bitsians it will be last 3 digits of first idno
	password = models.CharField(max_length=3) # Random generated 3 digit no.
	id1 = models.CharField(max_length=12, default="", verbose_name="Paritcipant 1 ID") #idno of first participant. Format- 15059
	id2 = models.CharField(max_length=12, default="",verbose_name="Paritcipant 2 ID") #idno of second participant
	money = models.IntegerField(default=start_money)

	def __unicode__(self):
		return self.team_no
