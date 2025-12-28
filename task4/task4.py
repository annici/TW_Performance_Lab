#python task4.py vector.txt

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_path",  help="Файл с массивом")
args = parser.parse_args()

vector=[]
#распаковываем массив:
try:
        with open((args.file_path).strip(), 'r', encoding='utf-8') as file:
            for _,row in enumerate(file):
                vector.append(int(row.strip()))
except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден")

'''
Наибыстрейший способ привести все элементы к одному числу - привести их к медиане,
т.к. именно сумма модулей разностей медианы и  чисел массива
sum(|v[i] - mediana|) минимальна;
если за один ход программы можно изменить только одно число и только на 1, то эта сумма и равна
мин. кол-ву ходов программы.
'''
import statistics
median = statistics.median(vector)
min_iterations= sum(abs(v - median) for v in vector)
if min_iterations > 20:
    print('20 ходов недостаточно для приведения всех элементов массива к одному числу')
else:
    print("Наименьшее количество ходов равно ", min_iterations)


