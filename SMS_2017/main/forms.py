from django.forms import *
from models import *

class BitsRegistrationForm(ModelForm):
	class Meta:
		model= Team
		fields= ['id1','id2']

class RegistrationForm(ModelForm):
	class Meta:
		model= Team
		fields= ['id1','id2','team_no']
		

