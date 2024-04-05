x = int(input('Введите целое число: '))
suma = 0
for i in range(1, x+1):
    print(i, end=' ')
    suma += i
print('\nСумма первых чисел =', suma)