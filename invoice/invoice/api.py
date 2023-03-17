from rest_framework.views import APIView
from rest_framework.response import Response
import time
from rest_framework.parsers import JSONParser
from models import Invoice, InvoiceDetail

class API(APIView):
    def get(self,request):
        pr = request.GET.get('invoice_no')
        package = {}
        try:
            in1 = Invoice.objects.get(invoice_no=pr)
            in2 = InvoiceDetail.objects.get(invoice=pr)
        except:
            print(aww)

        print(in1)
        print(in2)

        return Response("Lmao")

    def post(self,request):
        data = request.POST
        print(data)
