n = int(input())
sub = 1
print(sub)
while sub < n:
    if sub*2 < n:
        print(sub * 2)
        sub = sub*2
    else:
        break