def count_integer_numbers(a, b, c):
   
    integer_count = 0
    if a.is_integer():
        integer_count += 1
    if b.is_integer():
        integer_count += 1
    if c.is_integer():
        integer_count += 1
    return integer_count

def main():
 
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    integer_count = count_integer_numbers(a, b, c)

    print("Кількість цілих чисел:", integer_count)

if __name__ == "__main__":
    main()
