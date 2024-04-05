s = []
count = 0
n = 1

while n != 0:
    n = float(input())
    s.append(n)

for i in range(len(s) - 1):
    if s[i+1] < s[i]:
        count += 1

print('Уменьшение температуры произошло', count - 1, 'раз(а)')
