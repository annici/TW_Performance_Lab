flag=0
while flag==0:
    n,m =map(int,input("Введите размерность и длину обхода первого массива;\n n должно быть больше m для корректной работы программы: ").split())
    n2,m2 =map(int,input("Введите размерность и длину обхода второго массива;\n n должно быть больше m для корректной работы программы: ").split())
    if n<m or n2<m2:
        flag=0
    else:flag=1 #значения введены корректно, с массивами можно работать

def  functy(n,m):
    array = list(range(1,n+1))

    result_accum1='' #сюда будет записываться результат
    # [a:b] это первичные координаты интервала, последнее значение которого
    # будем сравнитьвать с 1:
    a=0
    b=m
    interval = array[a:b] #первичный интервал

    while interval[-1]!=1:
        result_accum1 += str(interval[0])
        a += m-1
        b += m-1

        array += (array)
        interval = array[a:b]
        if len(array)>100000:
            break
        elif interval[-1]==1:
            #print(interval)
            result_accum1 += str(interval[0]) #т.к. это последний проход цикла, надо сохранить рез-т
            #print('Выходим с результатом ',{result_accum1})

    return(result_accum1)

result=functy(n,m)+functy(n2,m2)
print(result)
