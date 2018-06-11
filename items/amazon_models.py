import time
import requests
from bs4 import BeautifulSoup
from .algorithms import *
import random
from .agent_list import user_agent_list
from .proxy_scraper import get_proxies, proxy_list
from itertools import cycle
from django.core.mail import send_mail
# from .TorCrawler import TorCrawler
# from .helper_function import parse_item
# Create Amazon item model

# crawler = TorCrawler()
proxies = get_proxies()
proxy_pool = cycle(proxies)


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

            #Set Proxy
            # proxy = random.choice(proxy_list)

            try:
                print(str(page) + " time to request the url")
                r = requests.get(url,
                                 headers=headers,
                                 # proxies={"http": proxy, "https": proxy},
                                 timeout=5)

                print("status_code: " + str(r.status_code))

                if int(r.status_code) == 200:
                    item_list = self.parse_item(r)

                print("--- %s seconds ---" % (time.time() - start_time))
            except:
                pass

        # sort item list by rating_count
        rating_count_sort = sorted(item_list, key=lambda x: x.rating_count, reverse=True)


        # sort top 10 rating_count_sort by rating
        rating_sort       = sorted(rating_count_sort[:10], key=lambda x: x.rating, reverse=True)

        return rating_sort






    def parse_item(self, response):

        list = []
        soup = BeautifulSoup(response.content, "html.parser")
        ul = soup.find('div', {'id': "resultsCol"})
        all_li = ul.find_all('li', class_='s-result-item')

        for li in all_li:
            all_a = li.find_all('a')
            rating_div = li.find('div', class_='a-column a-span5 a-span-last')
            if not rating_div:
                rating_div = li.find('div', class_='a-row a-spacing-top-mini a-spacing-none')
            try:
                price = li.find_all('span', class_='sx-price-whole')[0].text
                rating_count = int(rating_div.find_all('a')[1].text)
                rating = float(rating_div.find('i').text.split(" ")[0])
                title = all_a[1].text.strip()
                link = all_a[1]['href'] + "&tag=best10stoream-20"
                img = all_a[0].find('img')['src']

                if title and 'https' in link and not "Learn more about Sponsored Products." in title and len(
                        title) > 5:
                    new_item = Item()
                    new_item.title = title
                    new_item.link = link
                    new_item.rating = rating
                    new_item.rating_count = rating_count
                    # new_item.hotscore = int(calculate_customer_satisfaction_score(rating, rating_count))
                    new_item.image = img
                    new_item.price = price
                    list.append(new_item)
            except:
                pass

        return list












