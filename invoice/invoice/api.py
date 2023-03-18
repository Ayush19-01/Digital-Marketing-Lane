from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import time
import json
from invoice.models import Invoice, InvoiceDetail
from rest_framework import viewsets
from invoice.serializers import InvoiceSerializers
from rest_framework.decorators import api_view, renderer_classes

class InvoiceAPI(APIView):
    def get(self,request):
        try:
            x = request.GET.get("invoice_no")
        except:
            return Response("Invoice Number Not Found")
        try:
            instance = Invoice.objects.get(invoice_no=x)
            d = {"date":instance.date,"name":instance.cust_name, "invoice_no":instance.invoice_no}


        except:
            return Response("Information related to invoice number not found")
        return Response(d)
    def post(self,request):
        x = request.data
        dp_push = Invoice(invoice_no=x.get("invoice_no"),cust_name=x.get("cust_name"))
        dp_push.save()
        return Response("Data Pushed")
class InvoiceDetailAPI(APIView):
        def get(self,request):
            try:
                x = request.GET.get("invoice_no")
                print(x)
            except:
                return Response("Invoice Number Not Found")
            try:
                instance = InvoiceDetail.objects.get(invoice_no=x)
                print(instance)
                d = {"invoice_no": instance.invoice_no, "desc": instance.desc, "quantity": instance.quantity, "unit_price": instance.unit_price, "price": instance.price}


            except:
                return Response("Information related to invoice number not found")
            print(d)
            return Response(str(d))

        def post(self,request):
            x = request.data
            dp_push = InvoiceDetail(invoice_no=Invoice.objects.get(invoice_no=x.get("invoice_no")),desc=x.get("desc"),quantity=x.get("quantity"),unit_price= x.get("unit_price"),price=x.get("quantity")*x.get("unit_price"))
            dp_push.save()
            return Response("Data Pushed")



