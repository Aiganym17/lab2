# 1. Минимум из двух чисел
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a < b:
    print("Минимум:", a)
else:
    print("Минимум:", b)

# 2. Чётное или нечётное
num = int(input("Введите число: "))
if num % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")

# 3. Сумма чисел от 1 до N
N = int(input("Введите число N: "))
total = 0
for i in range(1, N + 1):
    total += i
print("Сумма чисел от 1 до", N, "равна", total)

# 4. Таблица умножения
N = int(input("Введите число N: "))
for i in range(1, 11):
    print(N, "*", i, "=", N * i)

# 5. Факториал числа
N = int(input("Введите число N: "))
fact = 1
for i in range(1, N + 1):
    fact *= i
print("Факториал числа", N, "равен", fact)

# 6. Количество гласных букв
text = input("Введите строку: ")
vowels = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Количество гласных букв:", count)

# 7. Разворот строки
text = input("Введите строку: ")
reversed_text = text[::-1]
print("Строка наоборот:", reversed_text)

# 8. Максимум в массиве
numbers = list(map(int, input("Введите числа через пробел: ").split()))
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("Максимум в массиве:", maximum)

# 9. Сумма элементов массива
numbers = list(map(int, input("Введите числа через пробел: ").split()))
total = 0
for num in numbers:
    total += num
print("Сумма элементов массива:", total)

# 10. Поиск числа X в массиве
numbers = list(map(int, input("Введите числа через пробел: ").split()))
X = int(input("Введите число для поиска: "))
found = False
for num in numbers:
    if num == X:
        found = True
        break
if found:
    print("Число", X, "найдено в массиве")
else:
    print("Число", X, "не найдено в массиве")
