"""
Created on Mon Sep 23 09:25:32 2019

@author: v.mazeiko
"""

from lxml import html
import requests

headers = {'User-Agent': 'Elinks/0.12pre6\
           (textmode; Linux 4.15.0-1047-aws x86-64; 157x62-3)'}

url = 'https://mail.ru/'

responce = requests.get(url, headers=headers) 
page = responce.content.decode('utf-8')
root = html.fromstring(page.text)

newsblock = page.xpath('//div[contains(@class,"news__list__item")]')

names = newsblock[0].xpath('//div[@class="news__list__item__link__text"]\
                             /a/text()')
hrefs = newsblock[0].xpath('//div[@class="news__list__item__link__text"]\
                             /a/@href')

