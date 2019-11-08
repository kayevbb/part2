import math

number = int (input ('Введиете свой возраст: '))

if number % 2 == 0 and number != 0:
    print ('2,4,6,8, и так до твоего возраста')
elif number == 0:
    print ('Zero is neither even, nor odd.')
else:
    print ('1,3,5,7,9, и так до твоего возраста')