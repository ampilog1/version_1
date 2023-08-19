# import requests
import json
# import pprint
#
# url_hh_areas = 'https://api.hh.ru/areas/113'
#
# # Получение списка городов в формате json
# req_areas = requests.get(url_hh_areas).json()
# params = {
#     'text': 'NAME:' 'python',
#     'area': '1',
#     'page': 0,
#     'per_page': 20
# }
# url_vacancies = 'https://api.hh.ru/vacancies'
# # Получение страницы с вакансиями и ее декодирование
# req_python = requests.get(url_vacancies, params).json()
# # data_content_decode = req_python.content.decode()
# # print(type(data_content_decode))
# # data_json = json.dumps(data_content_decode)
# # print(type(data_json))
# # pprint.pprint(data_json['items'])
# # data_text = req_python.text
# # data_json = json.loads(req_python)
with open('hh.json', 'r') as f:
    req_python = json.load(f)

with open('hh.txt', 'r') as f:
    req_python_txt = f.read()

data = []
keys = ['name', 'link', 'address', 'salary']

for item in req_python['items']:
    address = item['address']['raw'] if item['address'] is not None else 'нет адреса'
    salary = item['salary']['from'] if item['salary'] is not None else 'нет зарплаты'
    vacancy = dict(zip(keys, [item['name'], item['alternate_url'], address, salary]))
    data.append(vacancy)

# pprint.pprint(data)
#
#     # Заполнение словаря данными о вакансии из json
#     # data['name'] = item['name']
#     # data[-1]['link'] = item['alternate_url']
#     # data[-1]['address'] = item['address']['raw'] if item['address'] is not None else 'Адрес не указан'
#     # if item['salary'] is not None:
#     #     data[-1]['is_salary'] = True
#     #     data[-1]['salary_from'] = item['salary']['from']
#     #     data[-1]['salary_to'] = item['salary']['to']
#     # else:
#     #     data[-1]['is_salary'] = False
#
#
# with open('hh.json', 'w') as f:
#     json.dump(data, f, indent=4)
#
# pprint.pprint(data)
#
#
# #
# # f = open('hh.txt', 'w', encoding='utf-8')
# # f.write(str(req_python))
# # f.close()
a = 1
