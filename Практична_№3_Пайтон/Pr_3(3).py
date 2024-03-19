def check_triangle(angle_a, angle_b):

    if angle_a + angle_b < 180:
        print("Трикутник існує.")
        if angle_a == 90 or angle_b == 90:
            print("Трикутник прямокутний.")
        else:
            print("Трикутник не прямокутний.")
    else:
        print("Трикутник не існує.")

def main():

    angle_a = float(input("Введіть величину першого кута: "))
    angle_b = float(input("Введіть величину другого кута: "))

    check_triangle(angle_a, angle_b)

if __name__ == "__main__":
    main()
