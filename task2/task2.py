#python task2.py ellipse.txt dots.txt
import argparse

parser = argparse.ArgumentParser(description="Описалово")
parser.add_argument("ellipse",  help="Файл с параметрами эллипса")
parser.add_argument("dots", help="Файл с координатами точек")
args = parser.parse_args()


 #путь к файлу c координатами эллиспа
ellipsefile_path =(args.ellipse).strip()

#распаковываем параметры эллипса:
try:
        with open(ellipsefile_path, 'r', encoding='utf-8') as file:
            values=[]
            for row in file:
                values.extend(map(int, row.split()))

            #print(values)
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
dotfile_path =(args.dots).strip()

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
