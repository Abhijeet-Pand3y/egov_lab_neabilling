from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'index.html')

def branch_page(request):
    return render(request, 'branch.html')