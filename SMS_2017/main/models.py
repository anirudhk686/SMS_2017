from __future__ import unicode_literals
from django.db import models


start_money=1000000 #-----EDIT HERE ---------<complete> decide

class Team(models.Model):
	team_no = models.IntegerField(primary_key=True) #For bitsians first degree it will be last 5 digits of first idno
													#for other it will be 5 digit no. starting from 20001
	password = models.IntegerField() # Random generated 3 digit no.

	id1 = models.CharField(max_length=15)#For bitsians first degree -idno of first participant. Format- 15059
										 #for other can take name of particapants or their id
	id2 = models.CharField(max_length=15,default="") 
	money = models.IntegerField(default=start_money)

	def __unicode__(self):
		return str(self.team_no)


class StockList(models.Model):
	#This stores a list of all stocks that are going to be displayed
	#can be added directly in admin after efa gives the stocks
	name=models.CharField(max_length=50,unique=True)
	
	def __unicode__(self):
		return self.name


class Admin_control(models.Model):
	# only one instance to this model to be created in admin

	round_no = models.SmallIntegerField(default=0)		
	'''
	indicates transition period , round have values 1,2,3
	during which we can calculate final stock prices
	we can chage the rounds directly in admin
	'''
	
	setprice = models.BooleanField(default=False)
	# false - cannot setprice
	# true - can set price
	# we can chage the setprice directly in admin
	
	Other_teamno = models.IntegerField()
	# this will be used to assign team no to outstees during registration
	# this is used in otherRegistrationView
	def __unicode__(self):
		return "Admin_control"	

														

class Tradebook(models.Model):
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


class StockPrice(models.Model):
	#This will store the price of a stock for a particular round
	#It will ensure that there are no 2 prices for one stock in one round
	# we will have number of stocks* number of rounds objects
	
	stock=models.ForeignKey('StockList')
	round_no=models.PositiveSmallIntegerField()# no need to have as foriegn key as this model is mainly used to display prices on screen
	priceinitial=models.FloatField() #prices set by efa
	pricefinal=models.FloatField(default=0) #to be determined after each round
											#for first round priceinitial = pricefinal

	class Meta:
		unique_together=('stock','round_no',)

	def __unicode__(self):
		return str(self.stock) + '- Round '+ str(self.round_no)

