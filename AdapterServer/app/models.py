# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = "t_h_test"
    

class HSaleOrder(models.Model):
    customerID = models.IntegerField()
    productID = models.IntegerField()
    amount = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    status = models.IntegerField()
    deliverDeadline = models.DateField()
    createTime = models.DateTimeField()
    
    class Meta:
        db_table = "h_s_order"
        
class HSaleProduct(models.Model):
    productName = models.CharField(max_length=63)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productRemark = models.CharField(max_length=255)
    
    class Meta:
        db_table = "h_s_product"

class HSaleProductIntegration(models.Model):
    materialID = models.IntegerField()
    amount = models.IntegerField()
    
    class Meta:
        db_table = "h_s_product_integration"
        
class HSaleInventory(models.Model):
    amount = models.IntegerField()
    
    class Meta:
        db_table = "h_s_inventory"
        
class HPurchaseOrder(models.Model):
    providerID = models.IntegerField()
    materialID = models.IntegerField()
    amount = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    status = models.IntegerField()
    deliverDeadline = models.DateField()
    createTime = models.DateTimeField()
    
    class Meta:
        db_table = "h_p_order"

class HPurchaseMaterial(models.Model):
    materialName = models.CharField(max_length=63)
    materialRemark = models.CharField(max_length=255)
    
    class Meta:
        db_table = "h_p_material"

class HPurchaseInventory(models.Model):
    amount = models.IntegerField()
    
    class Meta:
        db_table = "h_p_inventory"

class HCustomer(models.Model):
    customerName = models.CharField(max_length=63)
    customerAddress = models.CharField(max_length=255)
    customerOC = models.CharField(max_length=20)
    customerContactor = models.CharField(max_length=63)
    customerContactPhone = models.CharField(max_length=12)
    
    class Meta:
        db_table = "h_customer"

class HProvider(models.Model):
    providerName = models.CharField(max_length=63)
    providerAddress = models.CharField(max_length=255)
    providerOC = models.CharField(max_length=20)
    providerContactor = models.CharField(max_length=63)
    providerContactPhone = models.CharField(max_length=12)
    
    class Meta:
        db_table = "h_provider"