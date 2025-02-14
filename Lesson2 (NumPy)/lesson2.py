import numpy as np

## Суммирование значений (и другие агрегатные функции)

rng = np.random.default_rng(1)
s = rng.random(50)

print(s)
print(sum(s))
print(np.sum(s)) # быстрее на больших объемах, считает сумму многомерных массивов

a = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])

print(np.sum(a)) # сумма всех элементов
print(np.sum(a, axis = 0)) # будут свернуты строки (сумма по столбцам)
print(np.sum(a, axis = 1)) # будут свернуты столбцы (сумма по строкам)

print(np.min(a))
print(np.min(a, axis = 0)) # мин строка
print(np.min(a, axis = 1)) # мин столбец

# другой вариант записи как метод np-массива
print(a.min())
print(a.min(0))

# безопасный вариант, который не выдаст ошибку в случае NaN значения
print(np.nanmin(a))
print(np.nanmin(a, axis = 0))
print(np.nanmin(a, axis = 1))


## Транслирование (broadcasting)
# набор правил, которые позволяют осуществлять бинарные операции (2 аргумента) с массивами разных форм и размеров

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])

print(a + b)
print(a + 5) # универсальная функция - независимо к каждому элементу
# число при помощи набора правил (транслирования) превращается в массив нужного размера (~b) 
# "5" транслируется в [5,5,5], т.е. подстраивается под размер массива

a = np.array([[0,1,2],[3,4,5]])
print(a + 5)

a = np.array([0,1,2])
b = np.array([[0], [1], [2]])

print(a + b)

# Правила:
# 1. Если размерности массива отличаются, то форма массива с меньшей размерностью дополняется единицей с левой стороны
# 2. Если формы массивов не совпадают в каком-то измерении, то если у массива форма равна 1, то он растягивается до соответствия формы второго массива
# 3. Если в каком-либо измерении размеры отличаются и ни один из них не равен 1, то генерируется ошибка

# пример1
a = np.array([[0,1,2], [3,4,5]])
b = np.array([5])
print(a.ndim, a.shape) 
print(b.ndim, b.shape)
# a         (2,3)
# b (1,) -> (1,1) -> (2,3)
print(a + b)

# пример2
a = np.ones((2,3), int)
b = np.arange(3)

print(a)
print(b)
print(a.ndim, a.shape) 
print(b.ndim, b.shape)

# a: (2,3)   (2,3)    (2,3)
# b: (3,) -> (1,3) -> (2,3)

c = (a + b)
print(c, c.ndim, c.shape)

# пример3
a = np.arange(3).reshape((3,1))
b = np.arange(3)

print(a, a.ndim, a.shape)
print(b, b.ndim, b.shape)

# (3,1) -> (3,1) -> (3,3)
# (3,)  -> (1,3) -> (3,3)

c = a + b

# [ 0 0 0 ]   [ 0 1 2 ]
# [ 1 1 1 ] + [ 0 1 2 ]
# [ 2 2 2 ]   [ 0 1 2 ]
print(c, c.ndim, c.shape)

# пример4
a = np.ones((3,2))
b = np.arange(3)

# 2 (3,2) -> (3,2) -> (3,2)
# 1 (3,)  -> (1,3) -> (3,3) -> ERROR

# --- см. дз №1 ---

X = np.array([
    [1,2,3,4,5,6,7,8,9],
    [9,8,7,6,5,4,3,2,1]
])

# Центрирование
Xmean0 = X.mean(0) # складываем столбцы
print(Xmean0)
Xcenter0 = X - Xmean0
print(Xcenter0)

Xmean1 = X.mean(1) 
print(Xmean1)
Xmean1 =  Xmean1[:, np.newaxis] # превратили массив в столбец, чтобы избежать ошибку транслирования
Xcenter1 = X - Xmean1
print(Xcenter1)


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.sin(x)**3 + np.cos(20 + y*x) * np.sin(y)
print(z.shape)

# import matplotlib.pyplot as plt

# plt.imshow(z)
# plt.colorbar()
# plt.show()
# ~ двумерное представление трехмерной функции


## Сравнения

x = np.array([1,2,3,4,5])
y = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(x < 3)
print(np.less(x,3))

# False = 0, True = 1
print(np.sum(x < 3)) # количество элементов
print(np.sum(y < 4, axis = 0 ))
print(np.sum(y < 4, axis = 1 ))
print(np.sum(y < 4))

# &, |, ^, ~ - побитовые операции, тоже через универсальные функции

# --- см. дз №2 ---


## Маски - булевые массивы
