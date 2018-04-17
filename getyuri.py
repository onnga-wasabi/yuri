import sys
import requests
from bs4 import BeautifulSoup
import re
from time import sleep
import pickle
import os
import cv2
import numpy as np


def crawl_urls(url):
    baseurl = 'https://matome.naver.jp'
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
    if not next_url[1:-1]:
        return 0
    sleep(2)
    crawl_urls(next_url[1:-1])


def save_image(url, dname, fname):
    content = get_image(url)
    fname = os.path.join(dname, fname + '.png')
    with open(fname, 'wb') as f:
        try:
            f.write(content)
        except:
            return 0
    return 0


def get_image(url):
    response = requests.get(url)
    try:
        soup = BeautifulSoup(response.text, 'lxml')
        #print('lxml parsed!')
    except:
        soup = BeautifulSoup(response.text, 'html5lib')
        print('html5lib parsed!')
    try:
        url = soup.find_all(class_='mdMTMEnd01Img01')[0]
    except:
        return 0
    url = re.sub('<a href=\"', '', re.sub('\" target.*/></a>', '', str(url.a)))
    return requests.get(url).content


def save_images(urls):
    return 0


if __name__ == '__main__':
    txt = 'YuriTakami.txt'
    with open(txt, 'r') as f:
        urls = f.readlines()
    for i, url in enumerate(urls):
        save_image(url, 'data/yuri', str(i))
