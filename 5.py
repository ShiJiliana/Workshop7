v_max = int(input())
for i in range(1, 1000000000):
    if i**3 < v_max:
        print(i**3, end = ' ')
        i += 1
    else:
        break

#another way
'''
n = int(input())
lenght = 1
while lenght**3 < n:
    print(lenght**3, end = ' ')
    lenght += 1
'''