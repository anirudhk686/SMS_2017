from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'register/bits',views.BitsRegistrationView), #Registration link for first degree bitsians
    url(r'register/other',views.RegistrationView), #Registration link for the rest
]