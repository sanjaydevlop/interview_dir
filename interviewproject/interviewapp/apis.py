from rest_framework.decorators import api_view
from django.db import transaction as tr
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from interviewapp.middlewares import check
from rest_framework import status
from interviewapp.models import InvoiceHeader,InvoiceItem,InvoiceSundry

# Each endpoint must accept the entire Invoice in one JSON during CRUD operation. That is, Each Invoice can have many InvoiceItems and InvoiceBillSundrys.


@api_view(["POST"])
def create_invoice(request):
    if(request.method=="POST"):
        request_data=request.data
        invoiceitems=request_data["invoiceitems"]
        date=request_data["date"]
        customer_name=request_data["customer_name"]
        billing_addr=request_data["billing_addr"]
        shippingaddr=request_data["shippingaddr"]
        gstin=request_data["gstin"]
        totalAmount=0

        InvoiceHeaderObject=InvoiceHeader.objects.create(
            date=date,
            customername=customer_name,
            billingaddr=billing_addr,
            shippingaddr=shippingaddr,
            gstin=gstin,
            totalamount=0
        )
        am=0
        for k in invoiceitems:
            item_name=k["item_name"]
            quantity=k["quantity"]
            price=k["price"]
            amount=quantity*price
            am+=amount        
            invoiceItem=InvoiceItem()
            invoiceItem.itemName=item_name
            invoiceItem.quantity=quantity
            invoiceItem.price=price
            invoiceItem.quantity=quantity
            invoiceItem.amount=amount
            invoiceItem.invoicerelated=InvoiceHeaderObject
            invoiceItem.save()
        InvoiceHeader.objects.filter(id=InvoiceHeaderObject.id).update(totalamount=am)

        return Response({"Success":"Success"},status=status.HTTP_201_CREATED)
    

@api_view(["GET"])
def getasingleInvoice(request,id):
    
    invoiceobj=InvoiceHeader.objects.get(id=id)
    if(invoiceobj.exists()):
        return Response({
            "invoiceid":invoiceobj.id,
            "date":invoiceobj.date,
            "customername":invoiceobj.customername
        })
    return Response({
        "Not found":"nt found"
    })


@api_view(["GET"])
def getamultipleInvoice(request):
    
    invoiceobjs=InvoiceHeader.objects.all()
    print(invoiceobjs)
    # print(invoiceobjs)
    # dt=[]
    # for k in invoiceobjs:
    #     dt.append({
    #         # "invoiceid":k.id,
    #         "date":k.date,
    #         "customername":k.customername
    #     })
    dt=[]
    return Response({"dt:":dt})









            





    
