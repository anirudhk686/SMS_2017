from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'register/bits',views.bitsRegistrationView), #Registration link for first degree bitsians
    url(r'register/other',views.otherRegistrationView), #Registration link for the rest
    url(r'trade',views.trade),# link to trade(buy/sell)
    url(r'setprice',views.setprice)
]