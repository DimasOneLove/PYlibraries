import numpy as np
import pandas as pd

# Pandas - расширение NumPy (структурированные массивы). Строки и столбцы индексируются метками, а не только числовыми значениями

# Series, DataFrame, Index - основные структуры Пандас


### Series

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
print(type(data))

print(data.values)
print(type(data.values))

print(data.index)
print(type(data.index))

print(data[0])
print(data[1:3])

data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])
print(data)
print(data['a'])
print(data['b':'d'])
print(type(data.index))

data = pd.Series([0.25, 0.5, 0.75, 1.0], index = [1, 10, 7, 'd'])
print(data)
print(data[1])
print(data[10:'d'])

population_dict = {
    'city_1': 1001,
    'city_2': 1002,
    'city_3': 1003,
    'city_4': 1004,
    'city_5': 1005,
}
population = pd.Series(population_dict)
print(population)
print(population['city_4'])
print(population['city_4':'city_5'])

# Для создания Series можно использовать
# - списки Python или массивы NumPy
# - скалярные значения
# - словари

# --- см. дз №1 ---


### DataFrame - двумерный массив с явно определенными индексами. Последовательность "согласованных" объектов Series

population_dict = {
    'city_1': 1001,
    'city_2': 1002,
    'city_3': 1003,
    'city_4': 1004,
    'city_5': 1005,
}

area_dict = {
    'city_1': 9991,
    'city_2': 9992,
    'city_3': 9993,
    'city_4': 9994,
    'city_5': 9995,
}
population = pd.Series(population_dict)
area = pd.Series(area_dict)
print(population)
print(area)

states = pd.DataFrame({
    'population1': population,
    "area1": area,
})
print(states)

print(states.values)
print(states.index)
print(states.columns)

print(type(states.values))
print(type(states.index))
print(type(states.columns))

print(states['area1'])

## DataFrame. Способы создания:
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив NumPy
# - структурированный массив NumPy

# --- см. дз №2 ---


### Index - способ организации ссылки на данные объектов Series и DataFrame. Index - неизменяем, упорядочен, является мультимножеством (могут быть повторяющиеся значения)

ind = pd.Index([2,3,5,7,11])
print(ind)
print(ind[1])
print(ind[::2])

# ind[1] = 5 -> ERROR

# Index - следует соглашениям объекта set (Python)

indA = pd.Index([1,2,3,4,5])
indB = pd.Index([2,3,4,5,6])
print(indA.intersection(indB))


### Выборка данных:

## 1) Из Series
data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])
print('a' in data)
print('z' in data)
print(data.keys())
print(list(data.items()))
data['a'] = 100
data['z'] = 1000
print(data)

## как одномерный массив
data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])
print(data['a':'c'])  # включая обе границы
print(data[0:2])  # а здесь как обычно в массиве (не включая 2)
print(data[(data > 0.5) & (data < 1)])
print(data[['a','d']])
print(data[1]) # индексы строчные -> 1 это индеккс для стандартного массива

data = pd.Series([0.25, 0.5, 0.75, 1.0], index = [1, 3, 10, 15])
print(data[1]) # выведется по индексу (из массива индексов), а не позиционный индекс стандартного массива
