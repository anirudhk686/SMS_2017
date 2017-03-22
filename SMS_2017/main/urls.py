from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^register/$',views.bitsRegistrationView), #Registration link for first degree bitsians
    url(r'^register/other$',views.otherRegistrationView), #Registration link for the rest
    url(r'^trade$',views.trade),# link to trade(buy/sell)
    url(r'^stocks/',views.stockList),
    url(r'^ranks/',views.teamRanks),
    url(r'admin_control',views.admin_control),
    url(r'^$',views.Dashboard),
    url(r'^exchange/',views.exchange),
    url(r'^team_details/',views.team_details),
]
