import random

# Генерація 10 випадкових чисел в діапазоні від 1 до 10
numbers = []
for i in range(10):
  numbers.append(random.randint(1, 10))

# Виведення чисел на екран
print("Випадкові числа:")
for number in numbers:
  print(number)

# Обчислення суми чисел
sum = 0
for number in numbers:
  sum += number

# Обчислення середнього арифметичного
average = sum / len(numbers)

# Виведення результату
print(f"Середнє арифметичне: {average}")
