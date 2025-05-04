# Задание 1

def get_palindromes(strings):
    # Используем лямбда-функцию для проверки на палиндром
    is_palindrome = lambda s: s == s[::-1]
    # Фильтруем исходный список, оставляя только палиндромы
    return list(filter(is_palindrome, strings))

# Пример использования
strings = ["level", "world", "deified", "python", "racecar", "hello"]
palindromes = get_palindromes(strings)
print(palindromes)  # ['level', 'deified', 'racecar']

print("\n") # Отступ в две строки


# Задание 2

def collatz_sequence(start):
    """Генератор для последовательности Коллатца."""
    if start <= 0:
        raise ValueError("Начальное число должно быть больше нуля.")

    current = start

    def next_collatz():
        """Вычисляет следующее число в последовательности Коллатца."""
        nonlocal current
        if current % 2 == 0:  # Четное число
            current //= 2
        else:  # Нечетное число
            current = current * 3 + 1
        return current

    while True:
        yield current
        if current == 1:
            break
        next_collatz()

### Пример использования:
# Создаем генератор
start_number = 168
for number in collatz_sequence(start_number):
    print(number)

print("\n")  # Отступ в две строки


# Задача 3

import math
import time

# Декоратор для определения времени выполнения функции
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        iterations = 100_000  # Количество повторений для более точного результата
        start_time = time.perf_counter()  # Точное измерение времени
        for _ in range(iterations):  # Повторяем функцию многократно
            result = func(*args, **kwargs)
        end_time = time.perf_counter()
        avg_time = (end_time - start_time) / iterations  # Среднее время выполнения одного вызова
        print(f"Среднее время выполнения функции '{func.__name__}': {avg_time:.16f} секунд")
        return result
    return wrapper

# Функция для вычисления квадратного корня с указанным направлением округления
@timing_decorator
def process_numbers(numbers, *, round_direction='nearest'):
    """
    Заменяет каждое число в списке его квадратным корнем с указанным направлением округления.

    :param numbers: Список целых чисел
    :param round_direction: Направление округления ('up', 'down', 'nearest')
    :return: Новый список с округленными квадратными корнями
    """
    if round_direction not in {'up', 'down', 'nearest'}:
        raise ValueError("round_direction должен быть 'up', 'down' или 'nearest'")

    result = []
    for num in numbers:
        if num < 0:
            raise ValueError("Невозможно вычислить квадратный корень для отрицательного числа")

        root = math.sqrt(num)
        if round_direction == 'up':
            result.append(math.ceil(root))
        elif round_direction == 'down':
            result.append(math.floor(root))
        else:  # 'nearest'
            result.append(round(root))

    return result

# Пример использования
numbers = [1, 2, 3, 4, 5, 16, 25, 50, 81, 1156, 123, 300]
print(f"Направление округления - ближайшее целое:")
print(process_numbers(numbers, round_direction='nearest'))  # Округление до ближайшего
print(f"Направление округления - вверх:")
print(process_numbers(numbers, round_direction='up'))  # Округление вверх
print(f"Направление округления - вниз:")
print(process_numbers(numbers, round_direction='down'))  # Округление вниз