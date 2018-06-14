from django.shortcuts import render
from dev_best10.settings import *
from .amazon_models import Item
from .tests import testParse
from rq import Queue
from worker import conn

q = Queue(connection=conn)


# Home Page
def item_list(request):
    if request.method == "POST":
        q_word = request.POST['query_word']

        if q_word:
            item = Item()
            search_result = item.get_items(q_word=q_word)


            context = {
             "item_list": search_result,

            }
            return render(request,'items/item_list.html', context)
        else:
            return render(request, 'items/item_list.html')
    else:
        return render(request,'items/item_list.html')
