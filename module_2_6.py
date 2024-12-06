from turtle import Turtle, Screen
import sys

numbers = int(input('Oh shit here we go again.. введи число от 1 до 20: '))

if numbers > 20:
    print('Ты по-моему что-то перепутал')
    sys.exit()
password = []
for i in range(1, 21):
    for j in range(i, numbers):
        if numbers % (i + j) == 0 and i != j:
            password.extend([i, j])

print('All my homies use this password: ', *password, sep='')

