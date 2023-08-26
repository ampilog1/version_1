import json

from parsers import *

parsers = (hh, superjob, zarplata)

vacancy = []
for pars in parsers:
    job = pars()
    vacancy += job

with open('vacancy.json', 'w', encoding='utf-8') as f:
    json.dump(vacancy, f,
              indent=4,
              ensure_ascii=False)