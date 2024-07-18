from django.urls import path, include
from rest_framework.routers import SimpleRouter
from interviewapp import apis
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('/create', apis.create_invoice, name='signup'),
    path('/<id>',apis.getasingleInvoice,name="getsingle"),
    path("/getallinvoices",apis.getamultipleInvoice,name="getamultipleInvoice")
]


