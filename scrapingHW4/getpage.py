#from bs4 import BeautifulSoup as BS
import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}

def getpage(url, headers=headers, params=None):
    print(f'starting connection with {url}')
    responce = requests.get(url, headers=headers, params=params)
    print(f'request code: {responce.status_code}\nurl: {responce.url} ')
    responce = responce.content
    if len(responce):
    	print('the responce is received')
    else:
    	print('the responce is empty')
    return responce