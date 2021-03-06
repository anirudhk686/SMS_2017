from __future__ import unicode_literals
from django.db import models

start_money = 100000


class Team(models.Model):
	team_no = models.IntegerField(primary_key=True) #For bitsians first degree it will be last 5 digits of first idno
													#for other it will be 5 digit no. starting from 20001
	password = models.IntegerField() # Random generated 3 digit no.

	id1 = models.CharField(max_length=20)#For bitsians first degree -idno of first participant. Format- 15059
										 #for other can take name of particapants or their id
	id2 = models.CharField(max_length=20,default="") 

	mobile_no = models.IntegerField(default=0) # to store outstee mobile number
											# for bitsians it will be 0
	money = models.IntegerField(default=start_money)

	net_worth = models.IntegerField(default = start_money) # money + their portfolio 

	def __unicode__(self):
		return str(self.team_no)

class ID(models.Model):
	# this model stores all the id's registered. this used to prevent same id's registration in multiple teams
	idno=models.IntegerField(primary_key=True)  


class StockInfo(models.Model):
	#This stores a list of all stocks that are going to be displayed
	#also stores number of stokes bought/sold in each round
	# -----NOTE - CREAETE NAME*ROUND INSTANCES USING THE SCRIPT initialscript.py-----------
	
	name=models.CharField(max_length=50)
	round_no = models.SmallIntegerField(default=0)
	left = models.IntegerField(default=0) # bought - add, sell - subtract
	priceinitial=models.FloatField() #prices set by efa
	pricefinal=models.FloatField(default=0) # to be determined after each round
											# for first round priceinitial = pricefinal
	stocktype = models.BooleanField(default=True) #  True - BSE
												  #  False - nasdac
	
	exchange_rate=models.FloatField(default=1) # 1 - if the stock is BSE else value provided by EFA


	class Meta:
		unique_together=('name','round_no')
	
	def __unicode__(self):
		return self.name + '- Round '+ str(self.round_no)


class Admin_control(models.Model):
	# only one instance to this model 
	# its object creation and initialization in initialscript.py 
	# we change these in admin_control view - whose template will only be displayed when admin in logged in

	round_no = models.SmallIntegerField(default=0)		
	#round have values 1,2,3 
	
	trade_enable = models.BooleanField(default=False)
	# false - cannot trade - can only set prices 
	# true - can trade - cannot set prices
		
	Other_teamno = models.IntegerField()
	# this will be used to assign team no to outstees during registration
	# this is used in otherRegistrationView
	total_teams = models.IntegerField(default=0) # keep a count of total number of teams registered

	starting_money = models.IntegerField(default=0)

	def __unicode__(self):
		return "Admin_control"	

														

class Tradebook(models.Model):
	# stores details of each trade
	team=models.ForeignKey('Team')
	stockname =models.CharField(max_length=50)
	call=models.BooleanField() #True = Buy and False = Sell
	num = models.IntegerField(default=0) # number of stocks to buy/sell
	round_no = models.PositiveSmallIntegerField()
	def __unicode__(self):
		return str(self.team)+'- Round '+ str(self.round_no)+'-stock-'+self.stockname


class StockLeft(models.Model):
	'''
	model that stores to no. of stock left for a particular stock of a particular team.
	this is used in while evaluating if the number of stock a person intends to sell is not more than the ones bought by him
	'''
	left = models.IntegerField()
	team_no = models.IntegerField()
	stockname = models.CharField(max_length=50)

	class Meta:
		unique_together=('stockname','team_no')

	def __unicode__(self):
		return self.stockname + '-team-'+str(self.team_no)

class Exchange_rate(models.Model):
	'''
	this model stores the exchange rate for each round
	'''
	round_no = models.SmallIntegerField(default=0)
	exchange_rate=models.FloatField(default=1)

	class Meta:
		unique_together=('round_no','exchange_rate')

	def __unicode__(self):
		return 'round - '+str(self.round_no)+'-exchange_rate - '+str(self.exchange_rate)




