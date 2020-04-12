from rest_framework.views import APIView
from rest_framework.response import Response
from generatefaker.db_models import *
from faker import Faker
from django.utils import timezone
import uuid
import os
import json

class faker(APIView):
    fake = Faker()

    response = {"success"}
  
    def get(self,request,format=None):
        try:
            self.generate_locationKey()
            self.generate_locations()
            self.generate_receiptMessages()
            self.generate_businesses()
            return Response(data=self.response, status=200, content_type="application/json")
            
        except Exception as e:
            return Response(data="Internal Server Error main " +str(e),status= 500, content_type="text/plain")


    def generate_locationKey(self):
        try:
            locationkeys = LocationKeys()
            
            fake = self.fake
        
            for i in range(1,8):
                key = fake.uuid4()

            locationkeys.access_token = key    
            locationkeys.save()
            return Response(data=self.response, status=200, content_type="application/json")
        except Exception as identifier:
            return Response(data="Internal Server Error Test" +str(identifier),status= 500, content_type="text/plain")

    def generate_locations(self):
        try:
            location = Location()
            location.name = "#1- Baldinos Giant Jersey Subs"
            location.save()

            location = Location()
            location.name = "#3- Baldinos Giant Jersey Subs"
            location.save()

            location = Location()
            location.name = "#4- Baldinos Giant Jersey Subs"
            location.save()

            location = Location()
            location.name = "#8- Baldinos Giant Jersey Subs"
            location.save()

            return Response(data=self.response, status=200, content_type="application/json")
        except Exception as identifier:
            return Response(data="Internal Server Error Test" +str(identifier),status= 500, content_type="text/plain")
            
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
            
    def generate_receiptMessages(self):
        try:
            fake = self.fake
            start_id = fake.random_number(digits=5, fix_len=True)

            for i in range(1,5):
                receiptMessages = ReceiptMessages()
                receiptMessages.business_id = start_id + (2 * i)
                receiptMessages.line_1 = "Test SCAN THIS BARCODE IN OUR APP FOR REWARDS!"
                receiptMessages.line_2 = "SCAN THIS BARCODE IN OUR APP FOR REWARDS!"
                receiptMessages.line_3 = "SCAN THIS BARCODE IN OUR APP FOR REWARDS!"
                receiptMessages.line_4 = "SCAN THIS BARCODE IN OUR APP FOR REWARDS!"
                receiptMessages.line_5 = "Tets SCAN THIS BARCODE IN OUR APP FOR REWARDS!"
                receiptMessages.created_at = timezone.now()
                receiptMessages.updated_at = timezone.now()
                receiptMessages.header = "Scan CAPAddicts Rewards within 24 hrs"
                receiptMessages.save()
           
            return Response(data=self.response, status=200, content_type="application/json")
        except Exception as identifier:
            return Response(data="Internal Server Error Test" +str(identifier),status= 500, content_type="text/plain")
   
