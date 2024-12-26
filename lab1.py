import math

def compute_factorial(n):
    """Вычисляет факториал числа n."""
    return math.factorial(n)

def main():
    while True:
        user_input = input("Пожалуйста, введите положительное целое число (или 'выход' для завершения): ")
        
        if user_input.lower() == 'выход':
            print("Завершение программы.")
            break
        
        try:
            number = int(user_input)
            if number < 0:
                print("Ошибка: Пожалуйста, введите положительное число.")
            else:
                result = compute_factorial(number)
                print(f"Факториал числа {number} равен {result}.")
        except ValueError:
            print("Ошибка: Ввод должен быть целым числом.")

if __name__ == "__main__":
    main()
