from django.shortcuts import render

# Create your views here.


def vendors(request):
    return render(request, 'vendor/vendors.html')
