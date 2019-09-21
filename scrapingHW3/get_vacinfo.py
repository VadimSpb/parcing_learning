from bs4 import BeautifulSoup as BS
from parcing_HH_page import get_info 
from append_vac import append_vac

def get_vacinfo(coll, soup):
    vacancies = soup.find_all('div', class_='vacancy-serp-item')
    for vacancy in vacancies:
        name, salary_min, salary_max, currency, link = get_info(vacancy)
        coll = append_vac(coll, name, salary_min, salary_max, currency, domain, link)
        name =  None
        salary_min = None
        salary_max = None
        currency  = None
        link =  None
    return coll