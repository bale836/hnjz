# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from models import HSaleOrder
from models import HSaleProduct, HSaleProductIntegration

# Initial the result message
result = {}
result['ResCode'] = "000"
result['Desc'] = "Success"

# Common method to check the request format
def chkRequestJson(request):
    reqFormat = request.META['CONTENT_TYPE']
    print reqFormat
    if reqFormat != "application/json":
        result['ResCode'] = "-1"
        result['Desc'] = "The request format  is not json."
        return result
    
    try:
        json.loads(request.body)
    except:
        result['ResCode'] = "-1"
        result['Desc'] = "The request format  is not json."
        return result
    
# create sale order
def createsaleorder(request):
    chkRequestJson(request)
    reqJsonBody = json.loads(request.body)
    
    # Input parameters check
    # End
    
    _customerID = reqJsonBody['customerID']
    _productID = reqJsonBody['productID']
    _amount = reqJsonBody['amount']
    _discount = reqJsonBody['discount']
    _deliverDeadline = reqJsonBody['deliverDeadline']
    
    saleOrder = HSaleOrder(customerID=_customerID, productID=_productID, amount=_amount,
                           total=1000, discount=_discount, status=0, deliverDeadline=_deliverDeadline,
                           createTime='2017-07-02 21:55:00')
    #saleOrder = HSaleOrder(orderID=1,customerID=1)
    saleOrder.save()
    return HttpResponse(json.dumps(result), content_type="application/json")

# query sale order
def querysaleorder(request):
    _tmpResult = chkRequestJson(request)
    if _tmpResult['ResCode'] == "-1":
        return HttpResponse(json.dumps(_tmpResult), content_type="application/json")
    reqJsonBody = json.loads(request.body)
    
    # Input parameters check
    # End
    
    _customerID = reqJsonBody['customerID']
    _productID = reqJsonBody['productID']
    
    if _productID != "":
        # TBD
        saleOrder = HSaleOrder.objects.get(customerID = _customerID, productID = _productID)
    else:
        # TBD
        #saleOrder = HSaleOrder.objects.get(customerID = _customerID)
        saleOrder = HSaleOrder.objects.get(customerID = "1")
    
    result['Data'] = saleOrder
    return HttpResponse(json.dumps(result), content_type="application/json")

# Modify sale order
def modifysaleorder(request):
    chkRequestJson(request)
    reqJsonBody = json.loads(request.body)
    
    # Input parameters check
    # End
    
    _orderID = reqJsonBody['orderID']
    _customerID = reqJsonBody['customerID']
    _productID = reqJsonBody['productID']
    _amount = reqJsonBody['amount']
    _discount = reqJsonBody['discount']
    _status = reqJsonBody['status']
    _deliverDeadline = reqJsonBody['deliverDeadline']
    
    # Get object where orderID = _orderID
    # Update object using these new parameters
    # Save
    saleOrder = HSaleOrder(customerID=_customerID, productID=_productID, amount=_amount,
                           total=1000, discount=_discount, status=0, deliverDeadline=_deliverDeadline,
                           createTime='2017-07-02 21:55:00')
    saleOrder.save()
    result = {}
    result['ResCode'] = "000"
    result['Desc'] = "Success"
    return HttpResponse(json.dumps(result), content_type="application/json")


# create sale product
def createsaleproduct(request):
    chkRequestJson(request)
    reqJsonBody = json.loads(request.body)
    
    # Input parameters check
    # End
    
    _productName = reqJsonBody['productName']
    _productPrice = reqJsonBody['productPrice']
    _productRemark = reqJsonBody['productRemark']
    
    saleProduct = HSaleProduct(productName=_productName, productPrice=_productPrice, productRemark=_productRemark)
    saleProduct.save()
    
    result = {}
    result['ResCode'] = "000"
    result['Desc'] = "Success"
    return HttpResponse(json.dumps(result), content_type="application/json")

# query sale order
def querysaleprodcut(request):
    chkRequestJson(request)
    reqJsonBody = json.loads(request.body)
    
    # Input parameters check
    # End
    
    _productID = reqJsonBody['productID']
    _productName = reqJsonBody['productName']
    
    if _productID != "":
        # TBD
        pass
    else:
        # TBD
        pass
    
    result = {}
    result['ResCode'] = "000"
    result['Desc'] = "Success"
    return HttpResponse(json.dumps(result), content_type="application/json")

# Modify sale order
def modifysaleproducct(request):
    chkRequestJson(request)
    reqJsonBody = json.loads(request.body)
    
    # Input parameters check
    # End
    
    _productID = reqJsonBody['productID']
    _productName = reqJsonBody['productName']
    _productPrice = reqJsonBody['productPrice']
    _productRemark = reqJsonBody['productRemark']
    
    # Get object where orderID = _orderID
    # Update object using these new parameters
    # Save
    
    result = {}
    result['ResCode'] = "000"
    result['Desc'] = "Success"
    return HttpResponse(json.dumps(result), content_type="application/json")

# create sale product integration
def createsaleproductItg(request):
    chkRequestJson(request)
    reqJsonBody = json.loads(request.body)
    
    # Input parameters check
    # End
    
    _productID = reqJsonBody['productID']
    _materialID = reqJsonBody['materialID']
    _amount = reqJsonBody['amount']
    
    saleProductIntegration = HSaleProductIntegration(productID=_productID, materialID=_materialID, amount=_amount)
    saleProductIntegration.save()
    
    result = {}
    result['ResCode'] = "000"
    result['Desc'] = "Success"
    return HttpResponse(json.dumps(result), content_type="application/json")

# query sale order
def querysaleprodcutItg(request):
    chkRequestJson(request)
    reqJsonBody = json.loads(request.body)
    
    # Input parameters check
    # End
    
    _productID = reqJsonBody['productID']
    _materialID = reqJsonBody['materialID']
    
    if _productID != "":
        # TBD
        pass
    else:
        # TBD
        pass
    
    result = {}
    result['ResCode'] = "000"
    result['Desc'] = "Success"
    return HttpResponse(json.dumps(result), content_type="application/json")

# Modify sale order
def modifysaleproducct(request):
    chkRequestJson(request)
    reqJsonBody = json.loads(request.body)
    
    # Input parameters check
    # End
    
    _productID = reqJsonBody['productID']
    _productName = reqJsonBody['productName']
    _productPrice = reqJsonBody['productPrice']
    _productRemark = reqJsonBody['productRemark']
    
    # Get object where orderID = _orderID
    # Update object using these new parameters
    # Save
    
    result = {}
    result['ResCode'] = "000"
    result['Desc'] = "Success"
    return HttpResponse(json.dumps(result), content_type="application/json")
