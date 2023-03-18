from django.db import models
class Invoice(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    invoice_no = models.IntegerField(primary_key=True)
    cust_name = models.CharField(max_length=50)


class InvoiceDetail(models.Model):
    invoice_no = models.ForeignKey('Invoice',on_delete=models.CASCADE)
    desc = models.CharField(max_length=300)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    price = models.FloatField()