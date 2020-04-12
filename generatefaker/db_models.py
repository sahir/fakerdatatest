from django.db import models

# Create your models here.

class LocationKeys(models.Model):
    id = models.IntegerField(primary_key=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
  
    class Meta:
        db_table = 'location_key'

class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'locations'

class ReceiptMessages(models.Model):
    id = models.IntegerField(primary_key=True)
    business_id = models.IntegerField()
    line_1 = models.CharField(max_length=255, blank=True, null=True)
    line_2 = models.CharField(max_length=255, blank=True, null=True)
    line_3 = models.CharField(max_length=255, blank=True, null=True)
    line_4 = models.CharField(max_length=255, blank=True, null=True)
    line_5 = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    header = models.CharField(max_length=255, blank=True, null=True)

    
    class Meta:
        db_table = 'receipt_messages'


class Businesses(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    loyalty_program_type  = models.CharField(max_length=255, blank=True, null=True)
    preferences = models.CharField(max_length=255, blank=True, null=True)
    stage = models.CharField(max_length=255, blank=True, null=True)
    restaurant_type = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True) 

    
    class Meta:
        db_table = 'businesses'