from django.shortcuts import render
from dev_best10.settings import *
from .amazon_models import Item
from .tests import testParse
from featured_products.models import Product
from rq import Queue
from worker import conn

q = Queue(connection=conn)


# Home Page
def home(request):

    products = Product.objects.all()


    context = {
        'products': products,
    }
    return render(request,'items/home.html', context)

def search_result(request):

    if request.method == "POST":
        q_word = request.POST['query_word']

        if q_word:
            item = Item()
            search_result = item.get_items(q_word=q_word)

            for product in search_result:
                new_product = Product()
                new_product.title = product.title
                new_product.link  = product.link
                new_product.image = product.image
                new_product.rating_count = product.rating_count
                new_product.rating = product.rating
                new_product.hotscore = product.hotscore
                new_product.price    = product.price
                new_product.category = q_word
                new_product.save()

            saved_search_result = Product.objects.filter(category=q_word)

            context = {
             # "item_list": search_result,
                'item_list': saved_search_result,
            }
            return render(request,'items/search_result.html', context)
        else:
            context = {
                "error" : "Please enter your search items"
            }
            return render(request,'items/search_result.html', context)


    return render(request, 'items/search_result.html')

