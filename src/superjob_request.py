#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json


url = 'https://api.superjob.ru/2.0/vacancies'
headers = {
    "X-Api-App-Id": "v3.r.137504985.cc7e8d483cc20413f71b6861b28a159c6ae08e93.d80f6ee44097a2e0e1c5b34a4d8021cbbe4dd446"}
params = {
    "catalogues": 48,
    "keyword": 'python',
    "town": '4',
    "count": '20'
}
# Получение страницы с вакансиями и ее декодирование
req_python = requests.get(url, headers=headers, params=params).json()

with open('superjob.json', 'w', encoding='utf8') as f:
    json.dump(req_python, f,
              indent=4,
              ensure_ascii=False)
