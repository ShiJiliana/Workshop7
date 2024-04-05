n, k, r = map(int, input().split())
day = 1
n_new = n
while n_new < r:
    n_new += n_new * (k / 100)
    day += 1
print(day)