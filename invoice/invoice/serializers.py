from rest_framework import serializers
from models import Invoice,InvoiceDetail

class InvoiceSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = ["date","invoice_no","cust_name"]
class InvoiceDetailSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ["desc","invoice_no","quantity","unit_price","price"]