import os
import sys
import pprint


# print(os.path.dirname(os.path.abspath('manage.py')))
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graduate_work.settings')


for key in os.environ:
    print(key, '=>', os.environ[key])
# print(sys.path)
# print(os.path.abspath('manage.py'))