from django.shortcuts import render
from dev_best10.settings import *
from .amazon_models import Item
from .tests import testParse
from .models import SearchItem
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
                new_item = SearchItem()
                new_item.title = product.title
                new_item.link  = product.link
                new_item.image = product.image
                new_item.rating_count = product.rating_count
                new_item.rating = product.rating
                new_item.hotscore = product.hotscore
                new_item.price    = product.price
                new_item.category = q_word
                new_item.save()

            saved_search_result = SearchItem.objects.filter(query_word=q_word)

            context = {
             "item_list": search_result,
                # 'item_list': saved_search_result,
            }
            return render(request,'items/search_result.html', context)
        else:
            context = {
                "error" : "Please enter your search items"
            }
            return render(request,'items/search_result.html', context)


    return render(request, 'items/search_result.html')

