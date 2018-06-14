import time
import requests
from .algorithms import *
import random
from .agent_list import user_agent_list
from lxml import html
from .xpath import *
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

        # Set item list
        item_list = []

        start_time = time.time()

        for page in range(1, 3):
            print('loop ' + str(page) + " page")

            # set user agent
            user_agent = random.choice(user_agent_list)
            headers = {
                'User-Agent': user_agent,
            }

            #Set Url
            pre_url = 'https://www.amazon.com/s?url=search-alias%3Daps'
            keyword_url = '&field-keywords=%s' % q_word
            url = pre_url + keyword_url + '&page={0}'.format(page)


            try:
                print(str(page) + " time to request the url")
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
                            raw_title = item.xpath(XPATH_TITLE)
                            if len(raw_title) > 0:
                                title = raw_title[0]

                            # Get the Link
                            raw_link = item.xpath(XPATH_LINK)
                            if len(raw_link) > 0:
                                link = raw_link[0]

                            # Get image
                            raw_image = item.xpath(XPATH_IMAGE)
                            if len(raw_image) >= 1:
                                image = raw_image[-1]

                            # Get rating counts
                            raw_rating_counts = item.xpath(XPATH_RATING_COUNT)
                            if len(raw_rating_counts) >= 1:
                                raw_rating_counts = raw_rating_counts[-1].text
                                rating_counts = int(raw_rating_counts.replace(',', ''))

                            # Get the ratings
                            raw_rating = item.xpath(XPATH_RATING)
                            if len(raw_rating) >= 1:
                                rating = float(raw_rating[-1].split("out")[0])



                            #Create new item then append to
                            new_item = Item()
                            new_item.title = title
                            new_item.link = link
                            new_item.image = image
                            new_item.rating_count = rating_counts
                            new_item.rating = rating


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

















