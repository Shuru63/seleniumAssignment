from django.urls import path
from Seleniumbackend.views import KeywordListCreateView

urlpatterns = [
     path('vpn-search/', KeywordListCreateView.as_view(), name='vpn-search'),
]
