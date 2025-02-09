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

np.random.seed(1)

x1 = np.random.randint(10, size = 3)
x2 = np.random.randint(10, size = (3, 2))
x3 = np.random.randint(10, size = (3, 2, 1))

print(x1)
print(x2)
print(x3)

# атрибуты массива
print(x1.ndim, x1.shape, x1.size) # чило разрерностей, размер каждой размерности, общий размер массива
print(x2.ndim, x2.shape, x2.size)
print(x3.ndim, x3.shape, x3.size)

#доступ к элементам массива
a = np.array([1,2,3,4,5])
print(a[0])
print(a[-2])
a[1] = 20
print(a)

a = np.array([[1,2], [3,4]])
print(a)
print(a[0,0])
print(a[-1, -1])
a[1, 0] = 100
print(a)

a = np.array([1,2,3,4,5])
b = np.array([1.0,2,3,4,5])

print(a)
print(b)

a[0] = 10
print(a)

a[0] = 10.123
print(a) # зафиксирован тип массива, изменение типа не происходит


### Срезы [start: finish: step], по умолчанию [1: shape: 1]

a = np.array([1,2,3,4,5,6])
print([x for x in a.shape], a.size)
print(a[:3])
print(a[3:])
print(a[1:5])
print(a[1:-1])
print(a[1::2])
print(a[::-1])

# --- см. дз № 7 ---

b = a[:3]
print(b)

b[0] = 100
print(a) # изменилось а
# срез - не копия, а ссылка

# --- см. дз № 8 ---

a = np.arange(1, 13)
print(a)
print(a.reshape(2,6))
print(a.reshape(3,4))

# --- см. дз № 9 ---