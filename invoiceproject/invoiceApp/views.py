from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from invoiceApp.models import Invoice
from invoiceApp.serializers import InvoiceSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
def invoice_list(request):
    if request.method=="GET":
        invoices=Invoice.objects.all()
        serializer=InvoiceSerializer(invoices,many=True)
        return Response(serializer.data)
    serializer=InvoiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def invoice_detail(request,pk):
    # invoice=get_object_or_404(Invoice,pk=pk)
    try:
        invoice=Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=InvoiceSerializer(invoice)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer=InvoiceSerializer(invoice,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    