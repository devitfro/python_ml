# task 1
# Користувач із клавіатури вводить чотиризначне число. Необхідно перевернути число та
# відобразити результат. 
user_value = int(input('Enter number: '))
user_value_str = str(user_value)
user_value_reversed = user_value_str[::-1]

if len(user_value_str) != 4:
  print('Enter correct number..')
else:
  print(user_value_reversed)

# task 2
# Користувач із клавіатури вводить тризначне число. Потрібно показати на різних рядках
# значення першого, другого та третього числа. Також потрібно показати на окремому рядку
# суму цих трьох чисел.
num = int(input('Enter number: '))

if len(str(abs(num))) != 3:
  print('Enter correct number..')
else:
  x_list = [int(x) for x in str(num)]
  total = 0
  count = 1

  for i in range(3):
    total += x_list[i]
    print(x_list[i])
  print(f'sum of {num} = {total}')

  for j in reversed(x_list):
    print(f'{count}st number = {j}')
    count += 1
    
# task 2
# Користувач із клавіатури вводить тризначне число. Потрібно показати на різних рядках
# значення першого, другого та третього числа. Також потрібно показати на окремому рядку
# суму цих трьох чисел.
num = int(input('Enter number: '))

if len(str(abs(num))) != 3:
  print('Enter correct number..')
else:
  a = num // 100
  b = (num // 10) % 10
  c = num % 10
  total = a + b + c
  print(f'sum of {num} = {total}')
  print(c)
  print(b)
  print(a)

# task 3
# Користувач вводить з клавіатури дві цифри з інтервалу 10 - 99. Необхідно створити число,
# що містить ці цифри, у такому порядку, перше число множиться на 7, друге число
# множиться на 9, а після цього вони змінюються місцями і результат виводимо на екран. 
num = int(input('Enter number in range(10-99): '))

x = 7
y = 9

if num < 10 or num > 99:
  print('Enter correct number ..')
else:
  digit_1 = num // 10
  digit_2 = num % 10
  
  digit_x = digit_1 * x
  digit_y = digit_2 * y
  
  new_num = int(str(digit_y) + str(digit_x))
  print(new_num)

# task 4
# Користувач вводить з клавіатури два тексти. На виході відображається кількість символів у
# тексті, а також який текст довший. 
text_1 = str(input('Enter str 1: '))
text_2 = str(input('Enter str 2: '))

print(f'text 1: {len(text_1)}')
print(f'text 2: {len(text_2)}')

if len(text_1) > len(text_2):
  print('text_1 is longer')
elif len(text_1) < len(text_2):
  print('text_2 is longer')
else: 
  print('the same')
  
# task 5
# Користувач вводить текст із клавіатури. На виході потрібно показати кожен третій знак у
# тексті. 
text = input('Enter text: ')
result = ''

for x in text[::3]:
  result = result + x
  
print(result)

# task 6
# Користувач вводить слово з клавіатури. Необхідно перевірити, чи збігається перша і остання
# літера цього слова.
word = str(input('Enter a word: '))
new_word = word.lower()

if new_word[0] == new_word[-1]:
  print('Happy')
else:
  print('Unhappy')