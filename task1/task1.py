import argparse

parser = argparse.ArgumentParser(description="Описалово")
parser.add_argument("n", type=int, help="Размерность 1го массива")
parser.add_argument("m", type=int, help="Число обходов по 1му массиву")
parser.add_argument("n2", type=int, help="Размерность 2го массива")
parser.add_argument("m2", type=int, help="Число обходов по 2му массиву")
args = parser.parse_args()

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
            if len(array)>10000:
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
    result=functy(args.n,args.m)+functy(args.n2,args.m2)
    print(result)
except ValueError:
    print("..путь не рассчитался")
    if result =='':
        print('Результат функции пуст')

