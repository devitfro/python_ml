# task 1
# Користувач із клавіатури вводить елементи списку:
# [2, 0, 1, 2, 5, 7, 8, -2, -3, -8, 2, 10, 15, 4, 4, 11, 0, 0, -10, -5, 3, 3, 7, 7, 20].
# Необхідно знайти:
# a) Скільки разів число 2 є у списку (необхідно при розрахунках рахувати числа за модулем); 
# b) Покажіть максимальне число зі списку;
# c) Покажіть мінімальне число зі списку;
# d) Зробіть сортування;
# e) Порахуйте кількість негативних чисел;
# f) Порахуйте кількість позитивних чисел;
# g) Порахуйте кількість нулів 0.
list_numbers = list(map(int, input('Введіть числа через кому:').split(',')))
print(list_numbers)
# a
count_2 = sum(1 for n in list_numbers if abs(n) == 2)
print("count 2: ", count_2)

# b
max_num = max(list_numbers)
print('max: ', max_num)

# c
min_num = min(list_numbers)
print('min: ', min_num)

# d
sorted_numbers = sorted(list_numbers)
print('sorted: ', sorted_numbers)

# e
neg_num_count =  sum(1 for n in list_numbers if n < 0)
print("negative: ", neg_num_count)

# f
pos_num_count = sum(1 for n in list_numbers if n > 0)
print("positive: ", pos_num_count)

# g
zero_count = list_numbers.count(0)
print('zero: ', zero_count)

# task 2
# Користувач із клавіатури вводить елементи списку:
# [5, 0, 1, 5, 10, 11, 15, 3, 18, 7, 2, 10, 8, 21, 19, 36, 5, 47].
# Необхідно знайти:
# a) Суму всіх чисел, що входять до списку;
# b) Кількість елементів, що входять до списку;
# c) Середнє значення елементів списку;
# d) Показати усі парні значення списку;
# e) Показати всі непарні значення списку.
list_numbers2 = list(map(int, input('Введіть числа через кому:').split(',')))
print(list_numbers2)
# a
print("sum: ", sum(list_numbers2))

# b
print("count: ", len(list_numbers2))

# c
avg = sum(list_numbers2) / len(list_numbers2)
print("avg: ", avg)

# d
even = [n for n in list_numbers2 if n % 2 == 0]
print("even: ", even)

# e
odd = [n for n in list_numbers2 if n % 2 != 0]
print("odd:", odd)

# task 3
# Користувач із клавіатури вводить елементи списку:
# [“Car”,”Cat”,”Dog”,”Word”,”Street”,”Tree”,”Free”,”Tax”,”House”,”Second”,”First”,”Lamp”,”Year”,”Joi
# n”,”Jump”,”Ice”,”Brother”,”Free”,”Word”,”Year”,”Page”].
# Необхідно знайти:
# a) Сортування списку;
# b) Кількість елементів, що входять до списку;
# c) Показати кожен третій елемент списку [“Car”, “Word”, ….];
# d) Додати до списку такі елементи "Play", "Game", "Movie", "Star";
# e) Видалити зі списку “First”, “Year”, “Ice”, “Street”;
# f) Показати список у зворотному порядку;
# g) Створити список, що складатиметься з елементів під індексами 2, 5, 7, 10, 15, 17, 19, 20.
words = ["Car","Cat","Dog","Word","Street","Tree","Free","Tax","House","Second",
         "First","Lamp","Year","Join","Jump","Ice","Brother","Free","Word","Year","Page"]

# a
print(sorted(words))

# b
print(len(words))

# c
print(words[::3])

# d
words.extend(["Play", "Game", "Movie", "Star"])

# e
for w in ["First", "Year", "Ice", "Street"]:
  while w in words:
    words.remove(w)
    
# f
print(words[::-1])

# g
indexes = [2, 5, 7, 10, 15, 17, 19, 20]
new_list = [words[i] for i in indexes if i < len(words)]
print(new_list)

# task 4
# Створіть за допомогою генератора списків список, які виведе всі значення з інтервалу,
# початок і кінець якого створюється у випадковому порядку.
# Підказка: при вирішенні використовуємо random, як варіант використовувати перший
# random в інтервалі від 0 до 10, а другий random від 50 до 60.
# Для отриманого списку порахуйте:
# a) Суму чисел;
# b) Максимальне число;
# c) Мінімальне число;
# d) Зробіть сортування за спаданням;
# e) Порахуйте суму чисел з цього інтервалу, які поділяються на 3 та 7;
# f) Знайдіть середнє значення чисел зі списку.
import random

start = random.randint(0, 10)
end = random.randint(50, 60)

nums3 = [i for i in range(start, end + 1)]
print(nums3)

print("sum: ", sum(nums3))
print("max: ", max(nums3))
print("min: ", min(nums3))
print("sorted: ", sorted(nums3, reverse=True))

sum_div = sum(n for n in nums3 if n % 3 == 0 and n % 7 == 0)
print("Кратні 3 і 7: ", sum_div)

avg = sum(nums3) / len(nums3)
print("avg: ", avg)

# task 5
# Користувач із клавіатури вводить текст:
# Необхідно знайти:
# a) Загальна кількість символів, що входять до тексту;
# b) Вивести слова довжина яких більше 8;
# c) Вивести слова довжина яких більша або дорівнює 4 і менше 8;
# d) Порахувати скільки разів зустрічається “and” у тексті;
# e) Порахуйте скільки слів у текст;
# f) Порахуйте скільки речень у тексті;
# g) Порахуйте скільки разів зустрічається буква “p” та “P” у тексті.
text = """Python is a popular programming language known for its simplicity and readability.
It has a wide range of applications and is used for web development, data analysis,
artificial intelligence, and more. Python's extensive libraries and frameworks make it
highly versatile, and its beginner-friendly syntax allows new programmers to quickly
learn and start coding. Its community-driven approach and vast resources make Python
a go-to language for both beginner and experienced developers."""

# a
print("symbols:", len(text))

# b
words = text.split()
print([w for w in words if len(w) > 8])

# c
print([w for w in words if 4 <= len(w) < 8])

# d
print("and:", text.lower().count("and"))

# e
print("words:" , len(words))

# f
sentences = text.count('.') + text.count('!') + text.count('?')
print("sentences: ", sentences)

# g
count_p = text.count('p') + text.count('P')
print("p + P:", count_p)