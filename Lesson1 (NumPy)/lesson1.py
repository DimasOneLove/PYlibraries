import numpy as np
import sys
import array

### Типы данных Python
# 1) Динамическая типизация
x = 1
print(type(x))
print(sys.getsizeof(x)) #28 байт

x = "hello"
print(type(x))
print(sys.getsizeof(x)) #46 байт

x = True
print(type(x))
print(sys.getsizeof(x)) #28 байт

l1 = list()
print(sys.getsizeof(l1)) #56 байт

l2 = list([1, 2, 3])
print(sys.getsizeof(l2)) #88 байт

l3 = list([1, "2", True])
print(sys.getsizeof(l3)) #88 байт
#Cнижается скорость обработки тк лист хранит разные типы данных

a1 = array.array('i', [1, 2, 3]) #Массив - похож на список, но с ограничением на тип данных
print(type(a1))
print(sys.getsizeof(a1)) #92 байт
# ---см. дз № 1, 2 ---

# Массив - способ хранения, а не обработки. А NumPy - предлагает свою обработку данных


### NumPy

a = np.array([1, 2, 3, 4, 5])
print(type(a), a)

# "повышающее" приведение типов
a = np.array([1.23, 2, 3, 4, 5])
print(type(a), a)

a = np.array([1.23, 2, 3, 4, 5], dtype = int) #задаем тип
print(type(a), a)

#могут храниться многомерные массивы
a = np.array([range(i, i+3) for i in [2, 4, 6]])
print(a)
print(type(a))

# Некоторые готовые конструкции:
a = np.zeros(10, dtype = int)
print(a, type(a))

print(np.ones((3,5), dtype = float))

print(np.full((4,5), 3.1415))

print(np.arange(0, 20, 2))

print(np.eye(4, dtype = int))

# --- см. дз № 3 - 6 ---


### Массивы

