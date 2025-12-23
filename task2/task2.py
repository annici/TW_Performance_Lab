# Запрашиваем путь к файлу c координатами эллиспа
ellipsefile_path =input("Введите путь к файлу с параметрами эллипса: ").strip()

#распаковываем параметры эллипса:
try:
        with open(ellipsefile_path, 'r', encoding='utf-8') as file:
            # Разбиваем строку на отдельные числа
            values = (file.readline().strip()).split()

            if len(values) != 4:
                raise ValueError(f"Ожидается 4 параметра элипса, получено {len(values)}")

            # Преобразуем строки в числа с плавающей точкой (для удобства расчётов)
            x_center = float(values[0])
            y_center = float(values[1])
            semi_axis_a = float(values[2])
            semi_axis_b = float(values[3])

except FileNotFoundError:
        print(f"Ошибка: файл '{ellipsefile_path}' не найден")
except ValueError as aa:
        print(f"Ошибка при обработке значений эллипса: {aa}")
except Exception as bb:
        print(f"Произошла ошибка на этапе распаковки файла эллипса: {bb}")

# .. и к файлу c координатами точек
dotfile_path =input("Введите путь к файлу с параметрами точек: ").strip()

#распаковываем параметры точек:
try:
        with open(dotfile_path, 'r', encoding='utf-8') as file:
            coordinates = []
            for _,row in enumerate(file):
                row=row.strip().split()
                if len(row) != 2:
                    raise ValueError(f"Ожидалось 2 координаты, получено {len(row)}")
                if not row:# Пропускаем пустые строки
                    continue
                x = float(row[0])
                y = float(row[1])
                if (x-x_center)**2/semi_axis_a**2 + (y-y_center)**2/semi_axis_b**2 > 1:
                    print(2) #снаружи
                elif (x-x_center)**2/semi_axis_a**2 + (y-y_center)**2/semi_axis_b**2 == 1 :
                    print(0)#на эллипсе
                elif  (x - x_center) ** 2 / semi_axis_a ** 2 + (y - y_center) ** 2 / semi_axis_b ** 2 < 1:
                    print(1)#внутри


except FileNotFoundError:
        print(f"Ошибка: файл '{dotfile_path}' не найден")
except ValueError as s:
        print(f"Ошибка при обработке данных: {s}")
except Exception as bb:
        print(f"Произошла какая-та ошибка во время распаковки файла с координатами точек: {bb}")

'''
try:
    print('Рассчитаем точки  на окружности')
import math
    print(1,';',(math.sqrt(-(1-x_center)**2/semi_axis_a**2+1)/semi_axis_b + y_center))
    print( (math.sqrt(-(8 - y_center) ** 2 / semi_axis_b ** 2 + 1) / semi_axis_a + x_center), ';',8)
    
except Exception as bb:
        print(f"упси! ошибочка при расчёте координат точек на элипсе: {bb}")
'''