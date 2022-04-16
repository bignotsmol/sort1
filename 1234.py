a = []
b = input('Введи имя участника')
while b != '0':
    a.append(b)
    b = input('Введи имя участника')
    
a.sort()
print(a)
