# SMS_2017
Stock Market Simulation, APOGEE 2017

##Requirements-  
Python 2.7 
Django 1.10

##IMPORTANT INSTRUCTIONS
1. stock data present in SMS_2017/stock_data.csv
2. before running server perform these actions

	a] python manage.py flush
	a] python initialscript.py  
		- important as this script populates the model as well as creates initial objects,assigns initial values

3. to change round, enable/disable trade - go to admin panel @ <server ip>/main/admin_control
	- note that you should have logged in django admin to view this page

4. while changing price after completion of round
	follow this order
	a) set trade_enable to false
	b) then change round
	c) then setprice
	d) set trade_enable to true

