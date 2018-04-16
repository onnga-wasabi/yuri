import sys
import requests
from bs4 import BeautifulSoup
import re
from time import sleep
import pickle
baseurl = 'https://matome.naver.jp'


def get_image_urls(url='/odai/2134131257162744701/2143315691256592103'):
    url = baseurl + url
    response = requests.get(url)
    try:
        soup = BeautifulSoup(response.text, 'lxml')
        #print('lxml parsed!')
    except:
        soup = BeautifulSoup(response.text, 'html5lib')
        print('html5lib parsed!')

    with open('YuriTakami.txt', 'a') as f:
        f.write(url + '\n')

    next_url = soup.find_all(class_='mdMTMEnd01Pagination01Next')
    next_url = re.sub('\".*a>', '', re.sub('<a.*href=\"', '', str(next_url)))
    if not next_url:
        return 0
    sleep(2)
    get_image_urls(next_url[1:-1])


if __name__ == '__main__':
    get_image_urls()
