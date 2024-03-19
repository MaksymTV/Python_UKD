def process_values(a, b):
    
    if a != b:
        a = max(a, b)
        b = max(a, b)
    else:
        a = 0
        b = 0
    return a, b


def main():
    a = int(input("Введіть a: "))
    b = int(input("Введіть b: "))

    a, b = process_values(a, b)

    print(f"a = {a}")
    print(f"b = {b}")


if __name__ == "__main__":
    main()