from bs4 import BeautifulSoup as BS
import numpy as np

from getpage import getpage
from parcing_HH_page import get_info #
from append_vac import append_vac
from get_vacinfo import get_vacinfo

domain = 'https://hh.ru'
url_pattern = domain + '/search/vacancy'
vacs = []

def hh_parcer():
	global domain
	global url_pattern 
	global vacs
	    
	payload = {'st':'searchVacancy',
	           'text':'Big data',
	           'specialization':['1.536', '1.3', '1.9', '1.10', '1.420', '1.25', 
	                 '1.395', '1.475', '1.82', '1.89', '1.110', '1.113', 
	                 '1.116', '1.137', '1.161', '1.172', '1.400', '1.203', 
	                 '1.211', '1.221', '1.225', '1.270', '1.272', '1.273', 
	                 '1.274', '1.50', '1.277', '1.474', '1.295', '1.117', 
	                 '1.296', '1.327', '1.359'],
	           'area':'113',
	           'salary':'',
	           'currency_code':'RUR',
	           'only_with_salary':'true',
	           'experience':'doesNotMatter',
	           'order_by':'relevance',
	           'items_on_page':'100',
	           'no_magic':'true',
	           'from':'suggest_post'}

	soup = getpage(url_pattern, params=payload)

	vacs = get_vacinfo(vacs, soup)

	next_page = soup.find_all('a', 'bloko-button HH-Pager-Controls-Next HH-Pager-Control', 'pager-next')
	next_page = domain + next_page[0].get('href')  

	while next_page  is not None:
	    soup = getpage(next_page, params=payload)
	    df = get_vacinfo(df, soup)

	    next_page = soup.find_all('a', 'bloko-button HH-Pager-Controls-Next HH-Pager-Control', 'pager-next')
	    if len(next_page) == 0:
	        break
	    print(next_page)
	    next_page = domain + next_page[0].get('href')
	return vacs