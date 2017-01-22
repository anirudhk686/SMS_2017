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

			idRegex=re.compile(r'(\d\d)(\d\d\d)')

			mo=idRegex.search(id1)
			
			team.team_no=mo.group(2)
			team.password=randint(101,999)
			team.save()
			form=BitsRegistrationForm()
		


	else:
		form=BitsRegistrationForm()

	return render_to_response('main/register.html',{'form':form})	