from django.urls import path
from invoiceApp import views

urlpatterns = [
    path('invoice/',views.invoice_list),
    path('invoice/<int:pk>/',views.invoice_detail)
]
