from __future__ import unicode_literals
from django.db import models


start_money=1000000 #<complete> decide

class Team(models.Model):
	team_no = models.PositiveIntegerField(primary_key=True)
	password = models.PositiveIntegerField()
	member1 = models.CharField(max_length=8)
	member2 = models.CharField(max_length=8,default="NONE")
	money = models.PositiveIntegerField(default=start_money)

	def __unicode__(self):
		return self.member1
