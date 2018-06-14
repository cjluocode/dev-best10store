import time
import requests
from .algorithms import *
import random
from .agent_list import user_agent_list
from lxml import html
from .helper_function import *
import toolz
# Create Amazon item model




class Item(object):
    def __init__(self):
        self.title = ''
        self.link  = ""
        self.rating = 5.0
        self.rating_count = 10
        self.hotscore = 90
        self.image    = ""
        self.price    = 1

    def get_items(self,q_word=None):
        start_time = time.time()

        # Set item list
        item_list = []


        for page in range(1, 3):
            print('loop ' + str(page) + " page")

            # set user agent
            user_agent = random.choice(user_agent_list)
            headers = {
                'User-Agent': user_agent,
            }

            #Set Url
            url = set_url(q_word,page)


            try:

                r = requests.get(url,
                                 headers=headers,
                                 timeout=5)

                print("status_code: " + str(r.status_code))

                if int(r.status_code) == 200:
                    try:
                        parser = html.fromstring(r.content)
                        all_item_container = parser.xpath(XPATH_ITEM_CONTAINER)

                        for item in all_item_container:

                            # Get the title
                            item_title = parse_title(item)

                            # Get the Link
                            item_link = parse_link(item)

                            # Get image
                            item_image_url = parse_image(item)

                            # Get rating counts
                            item_rating_counts = parse_rating_count(item)


                            # Get the ratings
                            item_rating = parse_rating(item)



                            #Create new item then append to
                            new_item = Item()
                            new_item.title = item_title
                            new_item.link = item_link
                            new_item.image = item_image_url

                            if item_rating_counts:
                                new_item.rating_count = item_rating_counts
                            if item_rating:
                                new_item.rating = item_rating


                            item_list.append(new_item)


                    except Exception as e:
                        print(e)

                print("--- %s seconds ---" % (time.time() - start_time))

            except:
                pass

        sorted_item_list = self.sort_item_list(item_list)

        return sorted_item_list


    def sort_item_list(self,item_list):

        #Remove duplicated item
        unique_item_list = toolz.unique(item_list, key=lambda x: x.title)

        # Sort item by rating_count
        rating_count_sort = sorted(unique_item_list, key=lambda x: x.rating_count, reverse=True)

        #Sort top 10 rating_count by rating
        rating_sort = sorted(rating_count_sort[:10], key=lambda x: x.rating, reverse=True)

        return rating_sort

















