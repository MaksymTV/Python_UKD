def count_positive_numbers(a, b, c):
    
    positive_count = 0
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    return positive_count

def main():

    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    positive_count = count_positive_numbers(a, b, c)

    print("Кількість додатніх чисел:", positive_count)

if __name__ == "__main__":
    main()
