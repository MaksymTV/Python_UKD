def calculate_values(x, y):

    if x < y:
        x = (x + y) / 2
        y = 2 * x * y
    else:
        y = (x + y) / 2
        x = 2 * x * y
    return x, y


def main():

    x = float(input("Введіть x: "))
    y = float(input("Введіть y: "))

    x, y = calculate_values(x, y)

    print(f"x = {x}")
    print(f"y = {y}")

if __name__ == "__main__":
    main()