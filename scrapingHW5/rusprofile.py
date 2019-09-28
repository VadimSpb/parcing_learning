# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:39:45 2019

@author: Vadim
"""
from lxml import html
import requests

#%%
patterns = {'main':'https://www.rusprofile.ru/id/',
         'founders':'https://www.rusprofile.ru/founders/',
         'connections':'https://www.rusprofile.ru/connections/',
         'finance':'https://www.rusprofile.ru/finance/',
         'contractors':'https://www.rusprofile.ru/contractors/4025637',
         'licenses':'https://www.rusprofile.ru/licenses/4025637',
         'okved': 'https://www.rusprofile.ru/okved/'}
         
id = '4025637'
url = patterns['main'] + id

#%%
def getpage(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
    responce = requests.get(url, headers=headers) 
    #page = responce.content.decode('utf-8')
    page = html.fromstring(responce.text)
    return page

#%%
page = getpage(url)
#%%

name = page.xpath("//div[@class='company-name']/text()")[0]
inn = page.xpath("//span[@id='clip_inn']/text()")[0]
registarion_date = page.xpath("//dl/dd[@class='company-info__text']/text()")[1]
staff = page.xpath("//dl/dd[@class='company-info__text']/text()")[2]
cheef = page.xpath("//a[@class='link-arrow gtm_main_fl']//span/text()")[0]
postzip = page.xpath("//address/span[@itemprop='postalCode']/text()")[0]
city = page.xpath("//address/span[@itemprop='addressRegion']/text()")[0]
adress = page.xpath("//address/span[@itemprop='streetAddress']/text()")[0]
