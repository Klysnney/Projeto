from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def sobre(request):
    return HttpResponse("Sobre")

def contatos(request):
    return HttpResponse("Contatos")

def receitas(request):
    return HttpResponse("Receitas")