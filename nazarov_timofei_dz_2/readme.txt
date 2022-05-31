Домашнее задание ко второму уроку.

Задание 1. ОК
#2й способ
result_1 = 15 * 3
result_2 = 15 / 3
result_3 = 15 // 2
result_4 = 15 ** 2
print('int', isinstance(result_1, int))
print('float', isinstance(result_2, float))
print('int', isinstance(result_3, int))
print('int', isinstance(result_4, int))

Задание 2. Решено через создание новых списков. Сложно.

Задание 3. Решено, сложно.
# Добавляем 0 к числам
# Добавляем кавычки, числа сохраняем в начале списка
# Вставляем числа между кавычками
# Выводим строку

Задание 4. ОК

Задание 5. ОК
import random
prices = []
for i in range(0, 15):
    price = round(random.uniform(1, 99), 2)
    prices.append(price)

price_kop = int(round(((price % 1)*100), 2))
price_rub = int(price // 1)
