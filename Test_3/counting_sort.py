"""
Реализация сортировки подсчетом.
Алгоритм сортировки подсчетом хорош тогда, когда сортируемый массив содержит больше элементов чем диапазон min - max
Т.е. например 20 тысяч эелементов от 0 до 100.
УСТОЙЧИВАЯ СОРТИРОВКА.

Лучшая верменная сложность - Ω(n+k)
Средняя временная сложность - Θ(n+k)
Худшая временная сложность - O(n+k)

Количество применяемой памяти - O(k)

Где k - разница между max и min элементом

(c) 2021 Kulikov Nikita, Saint-Petersburg, Russia
e-mail: pocketkurt@gmail.com
"""
# -*- coding: utf-8-*-


def counting_sort(arr):
    maximum = max(arr)  # максимальный элемент массива
    minimum = min(arr)  # минимальный элемент массива
    cnt = [0] * (maximum - minimum + 1)  # вспомогательный массив

    # если в массиве есть отрицательные числа
    if minimum < 0:
        for i in range(len(arr)):
            cnt[arr[i] + abs(minimum)] += 1

        pos = 0
        for num in range(len(cnt)):
            for k in range(cnt[num]):
                arr[pos] = num - abs(minimum)
                pos += 1
    # если в массиве числа от нуля
    elif minimum == 0:
        for i in range(len(arr)):
            cnt[arr[i]] += 1

        pos = 0
        for num in range(len(cnt)):
            for k in range(cnt[num]):
                arr[pos] = num
                pos += 1

    # если в массиве числа от положительного числа больше нуля
    else:
        for i in range(len(arr)):
            cnt[arr[i] - minimum] += 1

        pos = 0
        for num in range(len(cnt)):
            for k in range(cnt[num]):
                arr[pos] = num + minimum
                pos += 1
