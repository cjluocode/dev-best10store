from django.shortcuts import render
from .featured_product_scraper import FeaturedProduct
from .models import Product
# Create your views here.

def save_product(request):


    if request.method == "POST":
        query_word = request.POST['query_word']
        product = FeaturedProduct()
        product_list = product.get_products(query_word)

        #Save product list to django model
        for product in product_list:
            django_product = Product()
            django_product.title = product.title
            django_product.link = product.link
            django_product.rating = product.rating
            django_product.rating_count = product.rating_count
            django_product.hotscore    = product.hotscore
            django_product.price       = product.price
            django_product.image       = product.image
            django_product.category    = "Programming"

            django_product.save()


        context = {
            'product_list': product_list,
        }


        return render(request,'featured_products/save_product.html', context)

    return render(request,'featured_products/save_product.html')


