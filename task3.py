time = input('1: ').split()
time_2 = input('2: ').split()

list_time = []
list_time2 = []

for i in time:
    if i < 0:
        list_time.append(int(i))
    elif i > 0:
        print('Error')

for i in time_2:
    if i < 0:
        list_time2.append(int(i))
    elif i > 0:
        print('Error')

print(f'{list_time[0] - list_time2[0]}:{list_time[1] - list_time2[1]}:{list_time[2] - list_time2[2]}')
© 2019
GitHub, Inc.