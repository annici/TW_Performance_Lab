#python task3.py values.txt tests.txt report.json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("values",  help="Файл с оценками")
parser.add_argument("tests", help="Файл со структурой теста")
parser.add_argument("report", help="Файл-результат формата .json, заполненный оценками")
args = parser.parse_args()

import json
with open((args.values).strip(),'r', encoding='Utf-8') as values:
    values_loaded = json.load(values)['values'] #list
    values_as_dict={}
    for i in values_loaded: #формируем словарик типа "айди: оценка"
        values_as_dict |= {i['id']:i['value']}

with open((args.tests).strip(),  'r', encoding='Utf-8') as tests:
    tests_loaded = json.load(tests)

def iter_thrgh_dict(report_as_list,values_as_dict): #на вход list с тестами и dict с оценками

    for i_dict in report_as_list: #итерируем по словарям в списке
        if 'value' in  i_dict:
            i_dict['value']=values_as_dict[i_dict['id']]
        if 'values' in i_dict:
                try: # заходим в новый уровень вложенности и опять итерируем по словарям в новом списке
                    iter_thrgh_dict(i_dict['values'],values_as_dict)
                except KeyError as ww:
                    print(f"опять проблема с {ww}")
    return report_as_list #list

edited_tests=iter_thrgh_dict(tests_loaded['tests'],values_as_dict)

#в файл 'report' <- отредактированный 'tests':
with open((args.report).strip(), 'w') as file:
    json.dump({'tests':edited_tests}, file, indent=4)
