from rest_framework import serializers
from invoiceApp.models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    # handles converting model to json format
    class Meta:
        model=Invoice
        fields=('id','name','description','total','paid')