from django.shortcuts import render
from dev_best10.settings import *
from .amazon_models import Item
from .tests import testParse


# Home Page
def item_list(request):
    if request.method == "POST":
        q_word = request.POST['query_word']

        if q_word:
            item = Item()
            # FIRST SEARCH
            search_result = item.get_items(q_word=q_word)
            # Testing Mode // Backup  Search if first search len() == 0:
            # search_result = testParse(q_word=q_word)

            context = {
             "item_list": search_result,

            }
            return render(request,'items/item_list.html', context)
        else:
            return render(request, 'items/item_list.html')
    else:
        return render(request,'items/item_list.html')
