from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Keyword
from .serializers import KeywordSerializer
from Seleniumbackend.Script_selenum.vpn_search import change_vpn_location, perform_search

class KeywordListCreateView(APIView):
    def post(self, request):
        keyword = request.data.get("keyword")
        vpn_country = request.data.get("vpn_country")
        change_vpn_location(vpn_country)

        # Perform search
        result = perform_search(keyword)
        log = Keyword.objects.create(keyword=keyword, vpn_country=vpn_country, result=result)
        return Response(KeywordSerializer(log).data, status=status.HTTP_201_CREATED)
