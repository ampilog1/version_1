import json
import os
import sys
from parsers import *

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "graduate_work.settings"

import django
django.setup()

parsers = (hh, superjob, zarplata)

vacancy = []
for pars in parsers:
    job = pars()
    vacancy += job

with open('vacancy.json', 'w', encoding='utf-8') as f:
    json.dump(vacancy, f,
              indent=4,
              ensure_ascii=False)