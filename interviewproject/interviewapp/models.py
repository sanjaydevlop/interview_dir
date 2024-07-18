from django.db import models

# Create your models here.
class InvoiceHeader(models.Model):
    date=models.DateField()
    customername=models.CharField(max_length=100)
    billingaddr=models.CharField(max_length=100)
    shippingaddr=models.CharField(max_length=100)
    gstin=models.CharField(max_length=100)
    totalamount=models.DecimalField(max_digits=8,decimal_places=2)



class InvoiceItem(models.Model):

    itemName=models.CharField(max_length=100)
    quantity=models.DecimalField(max_digits=10,decimal_places=2)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    amount=models.DecimalField(max_digits=8,decimal_places=2)
    invoicerelated=models.ForeignKey(InvoiceHeader,on_delete=models.CASCADE)


class InvoiceSundry(models.Model):
    invoiceheader=models.ForeignKey(InvoiceHeader,on_delete=models.CASCADE)
    billSundryname=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10,decimal_places=2)



