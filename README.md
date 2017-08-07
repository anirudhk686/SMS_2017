# Stock Market Simulation, APOGEE 2017
This project was made for an event in our technical fest.This project was used as trading platform in an event which was simulation of the stock market.Participants could register and trade with their mobile.Server was hostel on college LAN.The event had four rounds and stock prices would change as per the trading in previous round.Also videoes were shown in between the rounds which simulated an event that would influence the market.More than 300 participants from all over the country participated in this event.

## Requirements  
- Python 2.7 
- Django 1.10

## Usage instructions
1. Stock data present in SMS_2017/stock_data.csv
2. Run `python3 manage.py createsuperuser` to have admin access.
3. Before running server perform these actions

	a) `python manage.py flush`<br>
	b) `python initialscript.py`<br> 
	- important as this script populates the model as well as creates initial objects,assigns initial values

4. to change round, enable/disable trade - go to admin panel @ <server ip>/main/admin_control
	- note that you should have logged in django admin to view this page

5. while changing price after completion of round follow this order:<br>
	a) set trade_enable to false<br>
	b) then change round<br>
	c) then setprice<br>
	d) set trade_enable to true<br>
	
