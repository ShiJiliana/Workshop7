s = input() #alphebetical
let = 2
#enumerate - создаёт пару из счётчика и элементов объекта
for i, c in enumerate(s):
    if i == let or i == let + 3:
        print(c, end = '')
        let += 3