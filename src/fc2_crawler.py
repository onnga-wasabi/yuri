import requests
from bs4 import BeautifulSoup
import re
import os
from time import sleep


def crawl_page_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    next_url = soup.find(class_='nav').a.get('href')
    if next_url == './':
        return 0
    return next_url


def crawl_image_url(url):
    url = url + '#more'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    img_list = []
    caps = soup.find_all(class_='cap')
    for cap in caps:
        a_list = cap.find_all('a')
        for a in a_list:
            img_list.append(a.get('href'))
    return img_list


def save_image(url, dname, fname):
    content = requests.get(url).content
    fname = dname + fname + '.png'
    with open(fname, 'wb') as f:
        f.write(content)
    return 0


def save_images(start, dname):
    next_url = start
    urls = []
    while not next_url == 0:
        urls.append(next_url)
        next_url = crawl_page_url(next_url)
        sleep(1)

    i = 0
    for url in urls:
        img_list = crawl_image_url(url)
        for img in img_list:
            save_image(img, dname, str(i))
            i += 1
            sleep(1)
    return 0


def main():
    save_images(START, DNAME)
    return 0


if __name__ == '__main__':
    START = 'https://yuritakami.blog.fc2.com/blog-entry-1894.html'
    DNAME = '../data/fc2/'
    main()
