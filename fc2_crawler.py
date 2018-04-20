import requests
from bs4 import BeautifulSoup
import re
import os
from time import sleep


def crawl_page_urls(url):
    response = requests.get(url)
    with open('fc2.txt', 'a') as f:
        f.write(url + '\n')
    try:
        soup = BeautifulSoup(response.text, 'lxml')
    except:
        soup = BeautifulSoup(response.text, 'html5lib')
        print('html5lib parsed!')
    next_url = soup.find_all(class_='nav')[0].a.get('href')
    if next_url == './':
        return 0
    sleep(1)
    crawl_page_urls(next_url)
    return 0


def crawl_image_url(url):
    url = url + '#more'
    print(url)
    response = requests.get(url)
    try:
        soup = BeautifulSoup(response.text, 'lxml')
    except:
        soup = BeautifulSoup(response.text, 'html5lib')
        print('html5lib parsed!')

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


def save_images(dname):
    txt = 'fc2.txt'
    with open(txt, 'r') as f:
        urls = f.readlines()
    i = 0
    for url in urls:
        img_list = crawl_image_url(url[:-1])
        for img in img_list:
            save_image(img, dname, str(i))
            with open('Donefc2.txt', 'a') as f:
                f.write(url+'\n')
            i += 1
            sleep(1)
    return 0


def main():
    dname = 'data/fc2/'
    save_images(dname)
    return 0


if __name__ == '__main__':
    '''
    start = 'https://yuritakami.blog.fc2.com/blog-entry-962.html'
    crawl_page_urls(start)
    '''
    main()
