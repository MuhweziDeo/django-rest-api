from django.conf.urls import url
from invoiceApp import views

urlpatterns = [
    url('invoice/',views.invoice_list),
    url('<int:pk>/',views.invoice_detail)
]
