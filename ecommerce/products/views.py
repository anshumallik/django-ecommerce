from django.shortcuts import render, get_object_or_404

from .models import Product, Category, Subcategory


# Create your views here.


def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=categories)
    context = {
        'products': products,
        'categories': categories,
        'category': category,
        'subcategories': subcategories,
    }
    return render(request, 'products/index.html', context)


def detail(request, category, subcategory, id):
    product = Product.objects.get(pk=id)
    context = {
        'product': product,
    }
    return render(request, 'products/detail.html', context)








