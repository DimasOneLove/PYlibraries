import numpy as np
import array
import sys
import random

### Array

## 1. Другие коды типов:
'''
Code       Python Type           Min bytes
'b'                int                   1
'B'                int                   1
'u'            unicode                   2
'h'                int                   2
'H'                int                   2
'i'                int                   2
'I'                int                   2
'l'                int                   4
'L'                int                   4
'f'              float                   4
'd'              float                   8
(Больший символы - без учета знака)
'''
## 2. Другие примеры:

a2 = array.array('u', ["1", "2", "3"])
print(type(a2))
print(sys.getsizeof(a2))
for char in a2:
    print(f"Символ: {char}, код: {ord(char)}")

a3 = array.array('f', [1.5, 2, 3])
print(type(a3))
print(sys.getsizeof(a3))


### NumPy

## 3. Создание массива с 5 значениями, располагающимися через равные интервалы в диапазоне от 0 до 1
print(np.linspace(0, 1, 5))

## 4. Создание массива с 5 равномерно распределенными случайными значениями в диапазоне от 0 до 1
print(np.random.uniform(0, 1, 5))

## 5. Создание массива с 5 нормально распределенными случайными значениями с мат ожиданием = 0 и дисперсией 1
print(np.random.normal(0, 1, 5))

## 6. Создание массива с 5 случайными целыми числами [0, 10)
print(np.random.randint(0, 10, 5))


### Срезы

## 7. Написать кода для создания срезов массива 3 на 4
# - первые две строки и три столбца
# - первые три строки и второй столбец
# - все строки и столбцы в обратном порядке
# - второй столбец
# - третья строка
np.random.seed(seed = 0)
arr = np.random.randint(10, size = (3,4))
print(arr)
print(arr[:2, :3])
print(arr[:3, 1:2])
print(arr[::-1, ::-1])
print(arr[:, 1:2])
print(arr[2:3, :])

## 8. Срез-копия
# с помощью .copy()
arr1 = np.random.randint(10, size = 8)
print(arr1)
arr2 = arr1[2:5].copy()
print(arr2)
print(arr1)
# с помощью np.array()
arr3 = np.array(arr2[::-1])
print(arr3)
print(arr2)

## 9. Использование newaxis для получения вектора-столбца и вектора-строки из массива
print(arr1)
vector_column = arr1[:, np.newaxis]
print(vector_column)

vector_row = arr1[np.newaxis, :]
vector_row1 = arr1[None, :] # newaxis == None
print(vector_row)
print(vector_row1)
