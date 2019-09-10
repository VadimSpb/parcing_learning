from bs4 import BeautifulSoup as BS
import numpy as np
import pandas as pd

from getpage import getpage
from newdf import newdf
from parcing_HH_page import get_info

### GET INFO HH.RU

def hh_parcer():
	domain = 'https://hh.ru'
	url_pattern = domain + '/search/vacancy'
	df = pd.DataFrame({
	    'Наименование вакансии': [],
	    'Предполагаемая зарплата (мин.)': [],
	    'Предполагаемая зарплата (макс.)': [],
	    'валюта': [],
	    'источник': [],
	    'ссылка на вакансию': []
	    })
	    

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

	def append_df(df, name, salary_min, salary_max, currency, domain, link):
	    df = df.append({
	            'Наименование вакансии': name,
	            'Предполагаемая зарплата (мин.)': salary_min,
	            'Предполагаемая зарплата (макс.)': salary_max,
	            'валюта': currency,
	            'источник': domain,
	            'ссылка на вакансию': link},
	            ignore_index=True)
	    return df

	def get_vacinfo(df, soup):
	    vacancies = soup.find_all('div', class_='vacancy-serp-item')
	    for vacancy in vacancies:
	        name, salary_min, salary_max, currency, link = get_info(vacancy)
	        df = append_df(df, name, salary_min, salary_max, currency, domain, link)
	        #name, salary_min, salary_max, currency , link =  None
	        name =  None
	        salary_min = None
	        salary_max = None
	        currency  = None
	        link =  None
	    return df

	soup = getpage(url_pattern, params=payload)
	df = get_vacinfo(df, soup)

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
	return df