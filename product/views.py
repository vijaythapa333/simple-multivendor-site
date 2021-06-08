import random # To get random products from the database

from django.shortcuts import render, get_object_or_404

from .models import Category, Product

from django.db.models import Q

# Create your views here.
def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    similar_products = list(product.category.products.exclude(id=product.id))

    # If more than 4 similar products, then get 4 random products 
    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)
    
    context = {
        'product': product,
        'similar_products': similar_products
    }

    return render(request, 'product/product.html', context)


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request,'product/category.html', {'category': category})


def search(request):
    query = request.GET.get('query', '') # second is default parameter which is empty
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'product/search.html', {'products':products, 'query': query})