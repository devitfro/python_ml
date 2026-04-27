# task 1
# Показати на екрані таблицю множення всіх чисел від 1 до 9. 
for i in range(1, 10):
  for j in range(1, 10):
    print(f"{i*j:3}", end=' ')
  print()
  
# task 2
# Використовуючи цикл for намалюйте наступну фігуру, якщо користувач задає розмір
# сторони та символ.
size = int(input("Сторона квадрата: "))
symbol = input("Символ: ")

for i in range(1, size + 1):
  if i % 2 != 0:
    print(symbol * size)
  else:
    print()
    
# task 3
# Використовуючи цикл for намалюйте наступну фігуру, якщо користувач задає розмір
# сторони та символ для парного та непарного рахунку
size = int(input("Сторона квадрата: "))
symbols = input("Символи через кому: ").split(',')
sym1 = symbols[0]
sym2 = symbols[1]

for i in range(1, size + 1):
  if i % 2 != 0:
    print(sym1 * size)
  else:
    print(sym2 * size)
    
# task 4
# Використовуючи цикл for намалюйте наступну фігуру, якщо користувач задає розмір
# сторони та символ
size = int(input("Сторона квадрата: "))
symbol = input("Символ: ")

for i in range(1, size + 1):
  spaces = size - i
  print(' ' * spaces + symbol)

# task 5
# Даний текст: “Hello Python! Hello User! How are you Python? I'm good, and you? Thank you, I'm
# good, too. Can you help me with task? Yes, sure. It's my task (show the code). I want to ask
# ChatGPT.”
# а) Порахуйте скільки речень у даному тексті;
# b) Порахуйте скільки прогалин у цьому тексті;
# c) Порахуйте скільки разів трапляється літера “a”;
# d) Переведіть цей текст у нижній регістр;
# e) Виведіть кожен 5-й символ цього тексту;
# h) Порахуйте довжину тексту і якщо вона парна вкажіть це, якщо непарна вкажіть це;
# i) Виведіть цей текст у зворотному порядку
text = "Hello Python! Hello User! How are you Python? I'm good, and you? Thank you, I'm good, too. Can you help me with task? Yes, sure. It's my task (show the code). I want to ask ChatGPT."

# a
sentences = text.count('.') + text.count('!') + text.count('?')
print("Речень:", sentences)

# b
spaces = text.count(' ')
print("Пробілів:", spaces)

# c
count_a = text.lower().count('a')
print("Буква 'a':", count_a)

# d
print(text.lower())
# e
print(text[4::5])

# h
length = len(text)

if length % 2 == 0:
  print("Довжина парна")
else:
  print("Довжина непарна")
  
# i
print(text[::-1])

# task 6
# Даний текст: “Our phone number + 38 (088) 125 67 92 і ми отримаємо від 9:00 to 18:00.”
# а) Порахуйте суму всіх чисел, що входять до цього тексту;
# b) Порахуйте суму всіх парних чисел, що входять до цього тексту;
# с) Порахуйте суму всіх непарних чисел, що входять до даних тексту;
# d) Порахуйте суму всіх чисел, що входять до цього тексту, які діляться на 3 без залишку
import re

text2 = "Our phone number + 38 (088) 125 67 92 і ми отримаємо від 9:00 to 18:00."

numbers = list(map(int, re.findall(r'\d+', text2)))
print("Числа:", numbers)
# a
print("Сума:", sum(numbers))

# b
even_sum = sum(n for n in numbers if n % 2 == 0)
print("Парні:", even_sum)

# c
odd_sum = sum(n for n in numbers if n % 2 != 0)
print("Непарні:", odd_sum)

# d
sum_3 = sum(n for n in numbers if n % 3 == 0)
print("Кратні 3:", sum_3)
