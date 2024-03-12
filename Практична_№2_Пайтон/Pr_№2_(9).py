#a 

def fibonacci(n):
  """
  Функція для обчислення n-го числа Фібоначчі.

  Args:
      n: Ціле число, що представляє порядковий номер числа Фібоначчі.

  Returns:
      Ціле число, що представляє n-е число Фібоначчі.
  """
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

start = 5
end = 20
for i in range(start, end + 1):
  print(f"Число Фібоначчі №{i}: {fibonacci(i - 1)}")


#b

for i in range(0, 21, 2):
  print(i)

for i in range(-1, -22, -3):
  print(i)
