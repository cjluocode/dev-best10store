import time
import requests
from bs4 import BeautifulSoup
from .algorithms import *
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

    def get_rectangle_items(self,q_word=None):

        item_list = []

        start_time = time.time()
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

        for page in range(1, 3):

            pre_url = 'https://www.amazon.com/s?url=search-alias%3Daps'
            keyword_url = '&field-keywords=%s' % q_word
            url = pre_url + keyword_url + '&page={0}'.format(page)

            r = requests.get(url, headers=headers, timeout=5)

            # sleep(5)while True:
            if int(r.status_code) == 200:
                print("looks great")

                soup = BeautifulSoup(r.content, "html.parser")

                ul = soup.find('div', {'id': "resultsCol"})
                all_li = ul.find_all('li', class_='s-result-item')

                for li in all_li:
                    all_a = li.find_all('a')
                    rating_div = li.find('div', class_='a-column a-span5 a-span-last')

                    if not rating_div:
                        rating_div = li.find('div', class_='a-row a-spacing-top-mini a-spacing-none')

                    if not rating_div:

                        rating_div = li.find('div', class_='a-row a-spacing-none')

                    try:
                        price = li.find_all('span',class_='sx-price-whole')[0].text
                        # decimal_price = li.find_all('span', class_='sx-price-fractional')[0]
                        # print(decimal_price)
                        rating_count = int(rating_div.find_all('a')[1].text)
                        rating = float(rating_div.find('i').text.split(" ")[0])
                        title = all_a[1].text.strip()
                        link = all_a[1]['href']
                        img = all_a[0].find('img')['src']

                        if 'https' in link and not "Learn more about Sponsored Products." in title and len(
                                title) > 5:
                            new_item = Item()
                            new_item.title = title
                            new_item.link = link
                            new_item.rating = rating
                            new_item.rating_count = rating_count
                            new_item.hotscore = int(calculate_customer_satisfaction_score(rating,rating_count))
                            new_item.image = img
                            new_item.price = price

                            item_list.append(new_item)
                    except:
                        pass

                print("--- %s seconds ---" % (time.time() - start_time))
            else:
                pass

        return sorted(item_list, key=lambda x: x.rating_count, reverse=True)

    # def get_square_items(self,q_word=None):
    #     print("sqaure items ")
    #     item_list = []
    #     start_time = time.time()
    #     headers = {
    #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    #
    #     for page in range(1, 3):
    #
    #         pre_url = 'https://www.amazon.com/s?url=search-alias%3Daps'
    #         keyword_url = '&field-keywords=%s' % q_word
    #         url = pre_url + keyword_url + '&page={0}'.format(page)
    #
    #         r = requests.get(url, headers=headers, timeout=5)
    #
    #         if int(r.status_code) == 200:
    #             print("looks great")
    #
    #             soup = BeautifulSoup(r.content, "html.parser")
    #             try:
    #
    #                 ul = soup.find('div', {'id': "resultsCol"})
    #
    #                 all_li = ul.find_all('li', class_='s-result-item')
    #
    #                 for li in all_li:
    #                     all_a = li.find_all('a')
    #                     rating_div = li.find_all('div', class_= "a-row a-spacing-none")
    #                     if not rating_div:
    #                         rating_div = li.find_all('div', class_="a-row a-spacing-none")
    #                         if not rating_div:
    #                             rating_div = li.find_all('div',class_='a-row a-spacing-top-mini')
    #
    #                     try:
    #                         rating_count = int(rating_div.find_all('a')[1].text)
    #                         print(rating_count)
    #
    #
    #
    #                     except:
    #                         pass
    #             except:
    #                 pass
    #
    #
    #
    #
    #
    #                 # try:
    #                 #     # rating_count = int(rating_div.find_all('a')[1].text)
    #                 #     # rating = float(rating_div.find('i').text.split(" ")[0])
    #                 #     title = all_a[1].text.strip()
    #                 #     link = all_a[1]['href']
    #                 #     img = all_a[0].find('img')['src']
    #                 #
    #                 #     if 'https' in link and not "Learn more about Sponsored Products." in title and len(title) > 5:
    #                 #
    #                 #         new_item = Item()
    #                 #         new_item.title = title
    #                 #         new_item.link = link
    #                 #         new_item.image = img
    #                 #         # new_item.rating_count = rating_count
    #                 #         # new_item.rating = rating
    #                 #         item_list.append(new_item)
    #                 # except:
    #                 #
    #                 #     pass
    #
    #         return  item_list












