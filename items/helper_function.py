#Set xpath
XPATH_ITEM_CONTAINER = "//div[@class='s-item-container']"
XPATH_TITLE_1 = ".//h2[@class='a-size-medium s-inline  s-access-title  a-text-normal']/text()"
XPATH_TITLE_2 = ".//h2[@class='a-size-base s-inline  s-access-title  a-text-normal']/text()"
XPATH_LINK  = ".//a[@class='a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal']/@href"
XPATH_IMAGE = ".//a[@class='a-link-normal a-text-normal']/img[@class='s-access-image cfMarker']/@src"
XPATH_RATING_COUNT_1 = ".//div[@class='a-row a-spacing-mini']/a[@class='a-size-small a-link-normal a-text-normal']"
XPATH_RATING_COUNT_2 = ".//div[@class='a-row a-spacing-top-micro']/a[@class='a-size-small a-link-normal a-text-normal']"
XPATH_RATING_COUNT_3 = ".//div[@class='a-row a-spacing-top-mini a-spacing-none']/a[@class='a-size-small a-link-normal a-text-normal']"
XPATH_RATING = ".//i[@class='a-icon a-icon-star a-star-4']/span[@class='a-icon-alt']/text()"


def parse_title(item):

    raw_title = item.xpath(XPATH_TITLE_1)
    if not raw_title:
        raw_title = item.xpath(XPATH_TITLE_2)


    if len(raw_title) > 0 :
        title = raw_title[0]
        return title
    else:
        return None


def parse_link(item):

    raw_link = item.xpath(XPATH_LINK)

    if len(raw_link) > 0:
        link = raw_link[0]
        if not link.startswith('http'):
            link = 'https://www.amazon.com' + link

        return link
    else:
        return None

def parse_image(item):

    raw_image = item.xpath(XPATH_IMAGE)
    if len(raw_image) >= 1:
        image = raw_image[-1]
        return image

    else:
        return None

def parse_rating_count(item):

    raw_rating_counts = item.xpath(XPATH_RATING_COUNT_1)

    if not raw_rating_counts:
        raw_rating_counts = item.xpath(XPATH_RATING_COUNT_2)
        if not raw_rating_counts:
            raw_rating_counts = item.xpath(XPATH_RATING_COUNT_3)


    if len(raw_rating_counts) >= 1:
        raw_rating_counts = raw_rating_counts[-1].text
        rating_counts = int(raw_rating_counts.replace(',', ''))

        return rating_counts

def parse_rating(item):

    raw_rating = item.xpath(".//span[@class='a-icon-alt']/text()")

    try:

        if "Prime" in raw_rating and len(raw_rating) >1:

            removed_prime_rating = [x for x in raw_rating if x != 'Prime']
            rating = float(removed_prime_rating[0].split("out")[0])

            return rating

        elif len(raw_rating) == 1:

            rating = float(raw_rating[0].split("out")[0])

            print(rating)
            return rating

    except Exception as e:
        print(e)




def set_url(q_word, page):
    pre_url = 'https://www.amazon.com/s?url=search-alias%3Daps'
    keyword_url = '&field-keywords=%s' % q_word
    amazon_url = pre_url + keyword_url + '&page={0}'.format(page)
    return amazon_url
