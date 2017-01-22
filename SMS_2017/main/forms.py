from django.forms import *
from models import *

class BitsRegistrationForm(ModelForm):
	class Meta:
		model= Team
		fields= ['id1','id2']
		

