#Данная функция присоединяет с списку словарь заданный значений

def append_vac(coll, name, salary_min, salary_max, currency, domain, link):
	    coll = coll.append({
	            'Наименование вакансии': name,
	            'Предполагаемая зарплата (мин.)': salary_min,
	            'Предполагаемая зарплата (макс.)': salary_max,
	            'валюта': currency,
	            'источник': domain,
	            'ссылка на вакансию': link})
	    return coll