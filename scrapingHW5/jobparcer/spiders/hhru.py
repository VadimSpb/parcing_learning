# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem
import re


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?text=pilot&area=113&st=searchVacancy']

    def parse(self, response: HtmlResponse):  # Метод парсинга - точка входа для паука
        next_page = response.css('a.HH-Pager-Controls-Next::attr(href)').extract_first()  # Ссылка у кнопки "Далее"
        yield response.follow(next_page, callback=self.parse)  # Переход на следующую страницу и вызов самой себя
        # Как только дошли до последней страницы идем дальше по коду
        vacancy = response.css(  # Ищем ссылку на вакансию и добавляем ее в наш список
            'div.vacancy-serp div.vacancy-serp-item div.vacancy-serp-item__row_header a.bloko-link::attr(href)').extract()
        for link in vacancy:  # Переходим по ссылкам на вакансии из полученного списка
            yield response.follow(link, callback=self.vacansy_parse)  # Вызываем метод для сбора инф-ции со страницы

    def vacansy_parse(self, response: HtmlResponse):
        name = response.css('div.vacancy-title h1.header::text').extract_first()  # Наименование вакансии
        salary = response.css('div.vacancy-title p.vacancy-salary::text').extract_first()  # Зарплата
        url = response.request.url
        source = 'hh.ru'
        yield JobparserItem(name=name, min_salary=salary,
                            max_salary=salary, url=url, source=source)  # Передаем сформированный item в pipeline