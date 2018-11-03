from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from invoiceApp.models import Invoice
from invoiceApp.serializers import InvoiceSerializer
from django.shortcuts import get_object_or_404
@api_view(['GET'])
def invoice_list(request):
    if request.method=="GET":
        invoices=Invoice.objects.all()
        serializer=InvoiceSerializer(invoices,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def invoice_detail(request,pk):
    # invoice=get_object_or_404(Invoice,pk=pk)
    try:
        invoice=Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=InvoiceSerializer(invoice)
    return Response(serializer.data)