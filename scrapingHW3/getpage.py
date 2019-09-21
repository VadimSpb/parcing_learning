from bs4 import BeautifulSoup as BS
import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
#params=None

def getpage(url, headers=headers, params=None):
	print(f'starting connection with {url}')
	responce = requests.get(url, headers=headers, params=params)
	print(f'request code: {responce.status_code}\nurl: {responce.url} ')
	print()
	soup  = BS(responce.content, "html.parser")
	return soup