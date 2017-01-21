from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
from random import randint

def register(request):
	context = RequestContext(request)
	registered = False

	if request.method == 'POST':
		T=Team()
		T.member1 = request.POST['member1']
		T.member2 = request.POST['member2']

		team_name = T.member1
		team_no = team_name[1:8]
		T.team_no = int(team_no)

		T.password = randint(1,99)
		T.save()
		registered=True    	

		form_dict = {'registered':registered,'team_no':T.team_no,'password':T.password}

		return render_to_response('main/register.html',form_dict,context)
		


	else:
		
		return render_to_response('main/register.html',context)