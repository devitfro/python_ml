# task 1
# Користувач із клавіатури вводить число від 1 до 7. На виході отримує назву дня тижня. Якщо
# користувач вводить число поза вказаним інтервалом, повідомити про помилку.

user_input = int(input('Enter number of day: '))
if user_input == 1:
  print('It\'s - MONDAY')
elif user_input == 2:
  print('It\'s - TUESDAY')
elif user_input == 3:
  print('It\'s - WEDNESDAY')
elif user_input == 4:
  print('It\'s - THURSDAY')
elif user_input == 5:
  print('It\'s - FRIDAY')
elif user_input == 6:
  print('It\'s - SATURDAY')
elif user_input == 7:
  print('It\'s - SUNDAY')
else:
  print('Incorrect number!')
  
# task 2
# Користувач з клавіатури вводить число від 1 до 12. На виході отримує назву пори року. Якщо
# користувач вводить число поза вказаним інтервалом, повідомити про помилку.
# user_input = int(input('Enter number of month: '))

months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  
if user_input > 0 and user_input <= 12:
  print('It\'s - ', months[user_input])
else:
  print('Incorrect number!')
  
# task 3
# Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у
# порядку зростання.

a = int(input('Enter number a: '))
b = int(input('Enter number b: '))

if a == b:
  print('The same numbers')
elif a < b:
  print(a, b)
else:
  print(b, a)

# task 4 
# Напишіть програму, яка на вхід приймає значення числа парне або непарне. А на виході
# показує чи вгадав користувач значення чи ні. Для написання програми використовуйте
# бібліотеку random в інтервалі від 1 до 1000 включно.

import random
user_input = input('Enter "парне" or "непарне": ')

random_number = random.randint(1, 1000)

if random_number % 2 == 0 and user_input == 'парне':
  print('Random number: ', random_number, '\nYou Win!')
elif random_number % 2 != 0 and user_input == 'непарне':
  print('Random number: ', random_number, '\nYou Win!')
else:
  print('Random number: ', random_number, '\nBot Win!')
  
# task 5 
# Напишіть програму, яка на вхід отримує значення швидкості в км/год (кілометри на
# годину), а на виході показує значення м/с (метри на секунду).

import math
num = float(input('Enter speed in km/hr: '))

km = 1000
hr = 3600

res = round(num * km / hr, 2)
print(f'{num} km/hr = {res} m/sec')

# task 6
# Напишіть програму, яка на вхід отримує значення кольору (red, green, yellow), а на виході
# вказує дії, які потрібно робити (stop, go, wait).

colors = {'red': 'stop', 'yellow': 'wait', 'green' : 'go'}
user_color = input('Enter color: ').lower()

if user_color == 'red':
  print(f'you must - {colors["red"]}')
elif user_color == 'yellow':
  print(f'you need - {colors["yellow"]}')
elif user_color == 'green':
  print(f'you can - {colors["green"]}')
else:
  print('Incorrect value!')
