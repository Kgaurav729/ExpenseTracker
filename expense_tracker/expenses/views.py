from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseListCreate(generics.ListCreateAPIView):
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializer

class ExpenseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializer