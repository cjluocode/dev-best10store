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

            context = {
             "item_list": search_result,
            }
            return render(request,'items/search_result.html', context)
        else:
            context = {
                "error" : "Please enter your search items"
            }
            return render(request,'items/search_result.html', context)


    return render(request, 'items/search_result.html')

