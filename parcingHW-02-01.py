import requests
import time
import random 
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as BS

pattern = 'https://icobench.com/icos'
last_page_num = 469

def pause():
    time.sleep(random.randint(1,5))

def load_pages(pattern):
    global last_page_num
    last_page_num += 1
    for i in range(1, last_page_num):
        param = {'page':i}
        page = requests.get(pattern, params=param,\
                            headers={'User-Agent': UserAgent().chrome})
        page.encoding = 'utf8'
        page = page.text
        soup = BS(page)
        soup = soup.text
#         while soup.status_code != 200:
#             pause()
#             load_pages(pattern)
        
        name = f'icobench_ico_page_{i}.html'
        with open(name, 'w', encoding='utf8') as output_file:
            output_file.write(page)
        pause()
    
load_pages(pattern)
