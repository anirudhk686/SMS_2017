from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *
from forms import *
from random import randint
import re

def BitsRegistrationView(request): #Registration for first degree bitsians

	if request.method == 'POST':
		form=BitsRegistrationForm(request.POST)

		if form.is_valid():
			team=form.save(commit=False)

			id1=form.cleaned_data['id1']

			team.team_no=id1
			
			team.password=randint(101,999)
			team.save()
			form=BitsRegistrationForm()
		


	else:
		form=BitsRegistrationForm()

	return render_to_response('main/bitsregister.html',{'form':form})	

def RegistrationView(request): #Registration for the rest

	if request.method == 'POST':
		form=RegistrationForm(request.POST)

		if form.is_valid():
			team=form.save(commit=False)
			team.password=randint(101,999)
			team.save()
			form=RegistrationForm()
		
	else:
		form=RegistrationForm()

	return render_to_response('main/register.html',{'form':form})	
