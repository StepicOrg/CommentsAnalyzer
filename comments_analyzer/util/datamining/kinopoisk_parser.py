import urllib.request
from bs4 import BeautifulSoup as soup

COMMENTS_LIST_URL = 'http://www.kinopoisk.ru/reviews/type/comment/status/{0}/period/year/perpage/100/page/{1}/'


def call(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    return opener.open(url).read().decode('windows-1251').encode('utf-8')


def download(cl, page):
    texts = []

    list_html = call(COMMENTS_LIST_URL.format(cl, page))

    list_dom = soup(list_html)
    for result in list_dom.find_all('div', {'class': 'brand_words'}):
        texts.append(result.p.span.text.replace('\n', ' ').replace('\r', ' '))

    return texts