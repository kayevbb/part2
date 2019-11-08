import math

num = int(input('Cколько классов: '))


for i in range(1,num+1):
    num_2 = int(input(f'Сколько студентов в {i} классе: '))
    print(f'Для студентов в {i} классе нужно {math.ceil(num_2 / 2)} парт')

print(f'Total: {total}')
