#%%
file_path =input("Введите путь к файлу с массивом: ").strip()
vector=[]
#распаковываем массив:
try:
        with open(file_path, 'r', encoding='utf-8') as file:
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
if median > 20:
    print('20 ходов недостаточно для приведения всех элементов массива к одному числу')
    print("Медиана найдена:", median)