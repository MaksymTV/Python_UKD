def find_divisors(a, b, c, k):
    
    divisors = []

    if a % k == 0:
        divisors.append("a")
    if b % k == 0:
        divisors.append("b")
    if c % k == 0:
        divisors.append("c")

    return divisors

def main():

    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
    k = float(input("Введіть число k: "))

    divisors = find_divisors(a, b, c, k)

    if divisors:
        print(f"{k} є дільником чисел {', '.join(divisors)}")
    else:
        print(f"{k} не є дільником жодного з чисел a, b, c.")

if __name__ == "__main__":
    main()