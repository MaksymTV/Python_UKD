import math

a = int(input("Введіть a: "))
b = int(input("Введіть b: "))
c = int(input("Введіть c: "))
d = int(input("Введіть d: "))

z = (a * math.sqrt(b) - c * math.sqrt(d)) / (a + b + c)

print("Z = ", z)
