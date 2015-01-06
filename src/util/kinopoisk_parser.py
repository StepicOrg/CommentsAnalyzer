import urllib.request
from bs4 import BeautifulSoup as soup


USER_REVIEW_URL = 'http://www.kinopoisk.ru{0}'
COMMENTS_LIST_URL = 'http://www.kinopoisk.ru/review/type/comment/status/{0}/period/year/perpage/100/page/{1}/'


def call(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    return opener.open(url).read().decode('windows-1251')


def download(cl, page):
    texts = []

    list_html = call(COMMENTS_LIST_URL.format(cl, page))

    list_dom = soup(list_html)
    for link in list_dom.find_all('div', {'class': 'more'}):
        review_html = call(USER_REVIEW_URL.format(link.a.attrs.get('href')))
        review_dom = soup(review_html)

        tr = review_dom.find('div', {'class': 'brand_words'})
        if tr is not None:
            str = ''
            for chunk in tr.find_all('p'):
                str += chunk.text

            print(str)
            texts.append(str.replace('\xa0', ' ').replace('\n', ' '))

    return texts