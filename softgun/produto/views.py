from django.shortcuts import render

# Create your views here.

def showprodutos(request):
    return render(request,'produtos.html')
