from django.shortcuts import render
from featured_products.models import Product
from items.amazon_models import Item
# Create your views here.

def home(request):
    products = Product.objects.filter(category="Business")
    item_list = []

    if request.method == "GET":
        category = request.GET.get('category')
        if category:
            products = Product.objects.filter(category=category)
            context = {
                'products': products,
            }
            return render(request,'landing_page/home.html', context)


    return render(request, 'landing_page/home.html', {'products':products})


def about(request):
    return render(request,'landing_page/about.html')


def contact(request):
    return render(request,'landing_page/contact.html')