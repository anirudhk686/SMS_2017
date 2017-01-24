from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *
from forms import *
from random import randint
import re





def bitsRegistrationView(request): #Registration for first degree bitsians

	if request.method == 'POST':
		
		team = Team()

		team.id1 = request.POST['id1']
		team.id2 = request.POST['id2']
		team.password=randint(101,999)
		team.team_no = int(team.id1)
		team.save()
    	#-------EDIT ADD JS ----------
		team_dict = {'team_no':team.team_no,'password':team.password}
		return render_to_response('main/test.html',team_dict)
		
	else:
		
		return render_to_response('main/bitsregister.html',)


def otherRegistrationView(request): #Registration for the rest

	if request.method == 'POST':

		team = Team()
		

		team.id1 = request.POST['id1']
		team.id2 = request.POST['id2']
		team.password=randint(101,999)

		#since outstees id may not be in 15474 pattern we assign them team nos starting form 20001
		#we increment the update the model once that number is assigned

		otherteamno = Admin_control.objects.all()[0]
		team.team_no = otherteamno.Other_teamno
		team.save()
		# increment teamno for next team
		otherteamno.Other_teamno += 1
		otherteamno.save()

    	#-------EDIT ADD JS ----------
		team_dict = {'team_no':team.team_no,'password':team.password}
		return render_to_response('main/test.html',team_dict)

		
	else:
		return render_to_response('main/otherregister.html',)	

def trade(request):
	stocklist1 = StockList.objects.all() 	#	getting all stock names
	
	if request.method == 'POST':

		roundno = Admin_control.objects.all()[0].round_no 	#	getting the round_no which entered by us in admin 
		if(roundno == 0): 		# 0 indicates trasition period for us to determine the stock prices - so no trading
			return HttpResponse("sorry,Cannot trade now")

		else:
			
			teamno = int(request.POST['teamno'])
			password = int(request.POST['password'])
			team = Team.objects.get(team_no=teamno)
			#authenticate
			if (team.password==password):

				action = int(request.POST['action'])
				stock_name = request.POST['stock']
				no_of_stock = int(request.POST['number'])
				
				# check if trader has enough stocks of that kind to sell

				if (action == 0): # if sell is not the call no need to calculate number of stocks left
					try:
						sl = StockLeft.objects.get(team_no=teamno,stockname=stock_name)
						stock_left = sl.left
					except StockLeft.DoesNotExist:
						sl = None
					
					if sl == None:
						stock_left=0
				

				if ((action == 0)and(stock_left <= no_of_stock )):	
					return HttpResponse("not enough stocks to sell")

				else:
					# store trade details in Trade model
					tradelog =  Tradebook()
					tradelog.team = team
					tradelog.stockname = stock_name
					if action==1:
						tradelog.call= True		#True = Buy and False = Sell
					else:
						tradelog.call= False
					tradelog.num =  no_of_stock
					tradelog.round_no = roundno
					tradelog.save()

					'''
					update the StockLeft model.
					if there is an existing entry for that stock and team - update the number of stock left
					else create an entry for that stock and team
					'''
					if action == 1:
						try:
							sl = StockLeft.objects.get(team_no=teamno,stockname=stock_name)
						except StockLeft.DoesNotExist:
							sl = None
					# if action == 0 , sl was already determined above
					# this division of one upand one done has been done to prevent fetching of the object 2 times in StockLeft database

					if sl == None:
						sl = StockLeft()
						sl.team_no=teamno
						sl.stockname = stock_name
						sl.left = no_of_stock # as first a stock must be bought before it is sold
					else:
						#update sl.left depending upon buy/sell
						if action==1: # stock bought
							sl.left = sl.left + no_of_stock
						else:
							sl.left = sl.left - no_of_stock

					sl.save()


					'''
					now affect changes in trader's account
					get price of that stock from StockPrice model
					'''

					s = StockList.objects.get(name=tradelog.stockname)
					sp= StockPrice.objects.get(stock=s,round_no=roundno).pricefinal

					if action == 1: #buy - so subtract money from trader's account
						team.money = team.money - (sp*tradelog.num)
					else:			# sell - add money to traders account
						team.money = team.money + (sp*tradelog.num)

					team.save()

					return HttpResponse("Trade success")
					

			else:
				return HttpResponse("Invalid teamno/password")

	else:
		
		return render_to_response('main/trade.html',{'stocklist':stocklist1})

def setprice(request):
	if request.method == 'POST':

		'''
		# determine price using Tradebook data 
		# save the prices to StockPrice model
		roundno = request.POST['round']# we cannot use from database as we would have set it 0
		stocklist = StockList.objects.all()
		
		# update StockPrice objects for this round for all stocks in StockList

		for s in stocklist:
			sp= StockPrice.objects.get(stock=s,round_no=roundno)
			# now to set its pricefinal we need to count to number of stocks bought/sold of that name in this round
			# we will use Tradebook data
			tb_buy = Tradebook.objects.filter(stockname=s.name,round_no=roundno)
			total=0# gives us total number of stock bought-sold
			for tb in tb_buy:
				if tb.call == True:
					total= total + tb.num
				else:
					total = total - tb.num

			# update the pricefinal depending upon total and priceinitial and total

			# -------EDIT HERE-------
			# Exact formulae to update

			sp.pricefinal = sp.priceinitial + ((total/100)*priceinitial)
			sp.save()
			'''

		return HttpResponse("Price set successful")


	else:
		set_price = SetPrice.objects.all()[0].setprice
		roundno = Round.objects.all()[0].round_no

		if ((set_price==True)and(roundno==0)):
			# prices can be set now 
			return render_to_response('main/setprice.html',)
		else:
			return HttpResponse("cannot set prices now")
