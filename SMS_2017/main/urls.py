from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'register/bits',views.BitsRegistrationView), #registration for first degree bitsians
]