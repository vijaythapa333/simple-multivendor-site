import random # To get random products from the database
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from .models import Category, Product

from django.db.models import Q

from .forms import AddToCartForm
from cart.cart import Cart


# Create your views here.
def product(request, category_slug, product_slug):
    # Create instance of Cart class
    cart = Cart(request)

    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    # Check whether the AddToCart button is clicked or not
    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            messages.success(request, "The product was added to the cart.")

            return redirect('product:product', category_slug=category_slug, product_slug=product_slug)            
    
    else:
        form = AddToCartForm()

    similar_products = list(product.category.products.exclude(id=product.id))

    # If more than 4 similar products, then get 4 random products 
    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)
    
    context = {
        'product': product,
        'similar_products': similar_products,
        'form': form,
    }

    return render(request, 'product/product.html', context)


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request,'product/category.html', {'category': category})


def search(request):
    query = request.GET.get('query', '') # second is default parameter which is empty
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'product/search.html', {'products':products, 'query': query})