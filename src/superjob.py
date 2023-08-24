#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import codecs
import pprint


with codecs.open('superjob.json', 'r', encoding='utf-8') as f:
    req_python = json.load(f)


data = []
keys = ['name', 'link', 'address', 'salary']

for item in req_python['objects']:

    address = item['address'] if item['address'] is not None else 'нет адреса'
    salary = item['payment_from'] if item['payment_from'] is not None else 'нет зарплаты'
    vacancy = dict(zip(keys, [item['profession'], item['link'], address, salary]))
    data.append(vacancy)

pprint.pprint(data)
#