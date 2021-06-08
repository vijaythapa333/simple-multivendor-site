from product.models import Category


def menu_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}