first, second, third = (int(input('Введите 1-ое число: ')), int(input('Введите 2-ое число: ')),
                        int(input('Введите 3-ье число: ')))
if first == second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
elif first != second != third:
    print ('0')