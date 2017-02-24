from django.http import HttpResponse, JsonResponse
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
		team.mobile_no = request.POST['contact']

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
	admin_object = Admin_control.objects.all()[0]#	getting the round_no which entered by us in admin_view
	roundno = admin_object.round_no
	stockinfo = StockInfo.objects.filter(round_no=roundno) 	#	getting all stock
	
	if request.method == 'POST':			
		
		tradeEnable = admin_object.trade_enable


		if (tradeEnable==False): 		# false indicates trasition period for us to determine the stock prices - so no trading
			return HttpResponse("sorry,Cannot trade now")

		else:
			
			teamno = int(request.POST['teamno'])
			password = int(request.POST['password'])
			
			#---- ADD EXCEPTION HANDLING HERE-----
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
				

				if ((action == 0)and(stock_left < no_of_stock )):	
					return HttpResponse("not enough stocks to sell")

				else:
					# store trade details in Trade model
					# --- NOTE IF EVENT NOT RUNNING EFFICIENTLY- WE CAN COMMENT THE TRADELOG PART-----

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
					update StockInfo model : field - number of stock left
					'''
					si = [e for e in stockinfo if e.name == stock_name]
					si = si[0]
					if action==1: # stock bought
						si.left = si.left + no_of_stock
					else:
						si.left = si.left - no_of_stock

					si.save()



					'''
					now affect changes in trader's account
					get price of that stock from StockPrice model
					'''

					sprice = si.pricefinal

					if action == 1: #buy - so subtract money from trader's account
						team.money = team.money - (sprice*no_of_stock)
					else:			# sell - add money to traders account
						team.money = team.money + (sprice*no_of_stock)

					team.save()

					return HttpResponse("Trade success")
					

			else:
				return HttpResponse("Invalid teamno/password")

	else:		

		return render_to_response('main/trade.html',{'stocklist':stockinfo})


def admin_control(request):
	'''
	---  IMPORTANT -----
	while changing price after completion of round
	follow this order
	a) set trade_enable to false
	b) then change round
	c) then setprice
	d) set trade_enable to true
	'''
	admin_object = Admin_control.objects.all()[0]

	if request.method == 'POST':
		# -------EDIT HERE------------------
		# ----- USE setprice()----
		return 

	else :

		current_round = admin_object.round_no
		trade_enable = admin_object.trade_enable

		return render_to_response('main/admin_control.html',{'current_round':current_round,'trade_enable':trade_enable})



def setprice(roundno):
	# determine prices using left field in StockInfo model
	# save the new prices to its pricefinal field 

	stockinfo = StockInfo.objects.filter(round_no=roundno)

	if (roundno == 1):
		# raise error
		# we set pricefinal = priceinitial for round 1 in initial.py script 
		return
	else:
		for s in stockinfo :
			# -------EDIT HERE-------
			# Exact formulae to update
			s.pricefinal = s.priceinitial + (s.left/1000)* s.priceinitial
			s.save()


def stockList(request):
	admin_control=Admin_control.objects.all()
	round_no=admin_control[0].round_no
	stocks=StockInfo.objects.filter(round_no=round_no)
	p={}
	for i in stocks:
		p[(i.name)]=[i.pricefinal,(i.pricefinal-i.priceinitial)]


	return JsonResponse(p, safe=False)

def teamRanks(request):
	players=Team.objects.all().order_by('money')
	p={}
	k=1
	for i in players:
		p[k]=[i.team_no,i.money]
	return JsonResponse(p, safe=False)



		



			

