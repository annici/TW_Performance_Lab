
n,m,n2,m2 =map(int,input("Введите размерность и длину массивов: ").split())

while  n<m or n2<m2 or n>50 or n2>50:
    n, m, n2, m2 = map(int, input("Значения введены некорректно;\n Введите сно :  ").split())

 # если значения введены корректно, с массивами можно работать

def  functy(n,m):
    array = list(range(1,n+1))

    result_accum1=''
    a=0
    b=m
    interval = array[a:b]
    try:
        while interval[-1]!=1:
            result_accum1 += str(interval[0])
            #.. значит, перемещаемся дальше:
            a += m-1
            b += m-1

            if b>=len(array):
                array += (array)
            interval = array[a:b]
            if len(array)>10000000000:
                print("Кажется, алгоритм нужно улучшить;\n либо попробуйте числа поменьше..")
                break
            elif interval[-1]==1:
                result_accum1 += str(interval[0])
    except TimeoutError:
        print("Кажется, алгоритм нужно улучшить;\n либо попробуйте числа поменьше..")
    except MemoryError:
        print("Кажется, алгоритм нужно улучшить;\n либо попробуйте числа поменьше..")

    return(result_accum1)

try:
    result=functy(n,m)+functy(n2,m2)
    print(result)
except ValueError:
    print("..путь не рассчитался")
    if result =='':
        print('Результат функции пуст')

