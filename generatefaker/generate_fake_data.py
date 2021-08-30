from rest_framework.views import APIView
from rest_framework.response import Response
from generatefaker.db_models import *
from faker import Faker
from django.utils import timezone
import uuid
import os
import json

# genreate fake data facker
class faker(APIView):
    fake = Faker()

    response = {"test"}
  
    def get(self,request,format=None):
        try:
            self.generate_businesses()
            return Response(data=self.response, status=200, content_type="application/json")
            
        except Exception as e:
            return Response(data="Internal Server Error main " +str(e),status= 500, content_type="text/plain")

   
    def generate_businesses(self):
        try:
            fake = self.fake
            
            for i in range(1,5):
                businesses = Businesses()
                businesses.name = "Baldinos"
                businesses.loyalty_program_type = "visit"
                businesses.preferences = ""
                businesses.stage = ""
                businesses.restaurant_type = "sit down restaurant"
                businesses.uuid = fake.uuid4()
                businesses.save()
            return Response(data=self.response, status=200, content_type="application/json")
        except Exception as identifier:
            return Response(data="Internal Server Error Test" +str(identifier),status= 500, content_type="text/plain")
            
   