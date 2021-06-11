from django.shortcuts import render

# Create your views here.
def cart_detail(request):
    return render(request, 'cart/cart.html')