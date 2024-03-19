def square_or_fourth_power(number):
  
  if number >= 0:
    return number ** 2
  else:
    return number ** 4

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

result_a = square_or_fourth_power(a)
result_b = square_or_fourth_power(b)
result_c = square_or_fourth_power(c)

print(f"a^2 = {result_a}")
print(f"b^2 = {result_b}")
print(f"c^2 = {result_c}")