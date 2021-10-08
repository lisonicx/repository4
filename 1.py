print ('введите размер массива:')
try:
    size = int(input())
except ValueError:
    print ('ошибка ввода данных')
else:
    if size<=0:
        print ('ошибка ввода данных')
    else:
        print ('введите элементы массива:')
        array = [0]*size
        for i in range(size):
            try:
                a = float(input())
            except ValueError:
                print ('ошибка ввода данных')
            else:
                array[i] = a
        print ('массив = ', end="")
        print (array)
        minimal = array[0]
        n = 0
        print ('введите delta:')
        try:
            delta = float(input())
        except ValueError:
            print ('ошибка ввода данных')
        else:
            for i in range(size):
                if array[i]<minimal:
                    minimal=array[i]
            for i in range(size):
                if (array[i] + delta == minimal) or (array[i] - delta == minimal):
                    n=n+1
            print ('количество элементов, отличающихся от минимального на delta, равно', n)
                

