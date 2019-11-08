num =  int ( input ( ' Введите свой номер: ' ))

def  work_with_namber ( num ):
    return  f ' Следующее число для числа { num } - { num + 1 } . Предыдущее число для число { num } равно { num - 1 } . '

print (work_with_namber (num))