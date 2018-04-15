import sys
import requests
from bs4 import BeautifulSoup
import re


def download(url='https://matome.naver.jp/odai/2134131257162744701'):
    response = requests.get(url)
    try:
        soup = BeautifulSoup(response.text, 'lxml')
        print('lxml parsed!')
    except:
        soup = BeautifulSoup(response.text, 'html5lib')
        print('html5lib parsed!')
    images=[]
    links=soup.find_all('img')
    for link in links:
        print(link)
        print()
    return 0


def main():
    download()
    return 0


if __name__ == '__main__':
    main()
