import sys
import requests
from bs4 import BeautifulSoup
import re
from time import sleep
import pickle
import os
import cv2
import numpy as np


def crawl_page_url(url):
    baseurl = 'https://matome.naver.jp'
    url = baseurl + url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        next_url = soup.find(class_='mdMTMEnd01Pagination01Next').get('href')
    except:
        return 0
    return next_url


def save_images(start, dname):
    baseurl = 'https://matome.naver.jp'
    next_url = start
    urls = []
    while not next_url == 0:
        urls.append(baseurl + next_url)
        next_url = crawl_page_url(next_url)
        sleep(1)

    i = 0
    for url in urls:
        print(url)
        if save_image(url, dname, str(i)) == 0:
            i += 1
        sleep(1)


def save_image(url, dname, fname):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        url = soup.find(class_='mdMTMEnd01Img01').a.get('href')
        sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            fname = dname + fname + '.png'
            print(fname)
            with open(fname, 'wb') as f:
                f.write(response.content)
            return 0
        return -1
    except:
        return -1


def main():
    save_images(START, DNAME)

    return 0


if __name__ == '__main__':
    START = '/odai/2134131257162744701/2143315691256592103'
    DNAME = '../data/naver/'
    main()
