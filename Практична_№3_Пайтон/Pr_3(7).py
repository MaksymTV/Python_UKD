def count_negative_numbers(a, b, c):
    
    count = 0
    if a < 0:
        count += 1
    if b < 0:
        count += 1
    if c < 0:
        count += 1
    return count

def main():
    a = int(input("Введіть a: "))
    b = int(input("Введіть b: "))
    c = int(input("Введіть c: "))

    count = count_negative_numbers(a, b, c)

    print(f"Кількість негативних чисел: {count}")

if __name__ == "__main__":
    main()