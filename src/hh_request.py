import requests
import json
import pprint

params = {
    'text': 'python',
    'area': '1',
    'page': 0,
    'per_page': 20
}

headers = {"X-Api-App-Id": "v3.r.137504985.cc7e8d483cc20413f71b6861b28a159c6ae08e93.d80f6ee44097a2e0e1c5b34a4d8021cbbe4dd446"}

url_vacancies = 'https://api.hh.ru/vacancies'
# url_vacancies = 'https://api.superjob.ru/2.0/vacancies'
# Получение страницы с вакансиями и ее декодирование
req_python = requests.get(url_vacancies, headers=headers, params=params).json()
# print(req_python)

with open('hh.json', 'w', encoding='utf8') as f:
    json.dump(req_python, f,
              indent=4,
              ensure_ascii=False)

f = open('hh.txt', 'w')
f.write(str(req_python))
f.close()