import json
import os
import sys
from parsers import *
from parsing_app.models import Vacancy


proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parsing_job.settings')

import django
from django.conf import settings
settings.configure(DEBUG=True)
django.setup()

parsers = (hh, superjob, zarplata)

vacancys = []
for pars in parsers:
    job = pars()
    vacancys += job

for vac in vacancys:
    v = Vacancy(**vac)
    v.save()


# with open('vacancy.json', 'w', encoding='utf-8') as f:
#     json.dump(vacancys, f,
#               indent=4,
#               ensure_ascii=False)