def calculate_distance(x, y):
    
    return (x ** 2 + y ** 2) ** 0.5


def main():
    # Запитуємо координати точок від користувача та конвертуємо їх у тип float.
    x1, y1 = map(float, input("Введіть координати точки A (x1, y1): ").split())
    x2, y2 = map(float, input("Введіть координати точки B (x2, y2): ").split())

    # Обчислюємо відстані від кожної точки до початку координат.
    distance_A = calculate_distance(x1, y1)
    distance_B = calculate_distance(x2, y2)

    # Порівнюємо відстані та виводимо результат.
    if distance_A < distance_B:
        print("Точка A ближче до початку координат.")
    elif distance_B < distance_A:
        print("Точка B ближче до початку координат.")
    else:
        print("Точки рівновіддалені від початку координат.")


if __name__ == "__main__":
    main()