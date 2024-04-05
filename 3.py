import math
for i in range(100000):
    n = int(input())
    sq = math.sqrt(n)
    int_sq = int(sq)
    if sq / int_sq != 1:
        print('Введите другое число')
    else:
        print(f'''Число {n} является полным квадратом''')
        break