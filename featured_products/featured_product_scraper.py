import time
import requests
import random
from .agent_list import user_agent_list
from lxml import html
from .helper_function import *
import toolz
# Create Amazon item model


class FeaturedProduct(object):

    def __init__(self):
        self.title = ''
        self.link  = ""
        self.rating = 5.0
        self.rating_count = 10
        self.hotscore = 90
        self.image    = ""
        self.price    = 1


    def get_products(self,q_word=None):

        start_time = time.time()

        # Set item list
        item_list = []


        for page in range(1, 3):
            print('loop ' + str(page) + " page")

            # set user agent
            headers = {
                'User-Agent': random.choice(user_agent_list),
            }

            #Set Url
            url = set_url(q_word,page)


            try:
                print("getting url")

                r = requests.get(url,
                                 headers=headers,
                                 timeout=5)

                print("status_code " + str(r.status_code))


                if int(r.status_code) == 200:
                    try:
                        parser = html.fromstring(r.content)
                        all_item_container = parser.xpath(XPATH_ITEM_CONTAINER)


                        for item in all_item_container:

                            # Parse the title,link,image,rating_count,rating
                            item_title = parse_title(item)
                            item_link = parse_link(item)
                            item_image_url = parse_image(item)
                            item_rating_counts = parse_rating_count(item)
                            item_rating = parse_rating(item)


                            #Create new item then append to
                            new_item = FeaturedProduct()
                            new_item.title = item_title
                            new_item.link = item_link
                            new_item.image = item_image_url

                            if item_rating_counts:
                                new_item.rating_count = item_rating_counts
                            if item_rating:
                                new_item.rating = item_rating
                                new_item.hotscore = get_hotscore(item_rating)


                            item_list.append(new_item)


                    except Exception as e:
                        print(e)

                print("--- %s seconds ---" % (time.time() - start_time))

            except Exception as e:
                print(e)

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

















