from pprint import pprint
from lxml import html
import requests
main_link = 'https://www.kinopoisk.ru/' #Основная ссылка на сайт
req = requests.get(main_link + 'afisha/new/city/1/') #Ссылка на фильмы в кинотеатрах
root = html.fromstring(req.text)

films_block = root.xpath('//div[contains(@class,"filmsListNew")]')


hrefs = films_block[0].xpath('//div[@class="name"]/a/@href')
names = films_block[0].xpath('//div[@class="name"]/a/text()')
genre = films_block[0].xpath('//div[@class="gray"][last()]/text()')
rating = films_block[0].xpath('//div[@class="rating"]/span/text()')

